import cloudinary.uploader
from django.shortcuts import render,redirect
from . models import *
from user.models import Profile
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import cloudinary



# Create your views here.

# Get All Blogs from DB
def index(request):
     blogs = Blog.objects.all().order_by('-createdAt')
     context = {
          'blog': blogs
     }
     return render(request, "blog/all_post.html", context)


# Get The Single Blog Post By The Blog Id
def single_blog_post(request, id):
     single_blog_post = Blog.objects.get(id = id)
     blog_comment = Comment.objects.filter(blog=single_blog_post)

     # Get blog Comments
     single_blog_page_comment = get_single_blog_comment(request, single_blog_post)
     
     # Create blog comment
     create_blog_comment(request, single_blog_post)
     
     # Get Total Comment per Blog
     get_total_comment_per_blog(request, single_blog_post)
     
     # Get the total Replies Per Comments
     for single_comment in blog_comment:
          get_total_replies_per_comment(request, single_comment.id)
     
     # Get Comment Replies
     comment_reply = get_comment_replies(request, single_blog_post)
     if comment_reply:
          return render(request, 'blog/replies.html', comment_reply)
     
     # Blog Like Status
     liked_user = single_blog_post.likes.filter(username=request.user).exists()
     like_status = False
     if liked_user:
          like_status = 'checked'
     else:
          like_status = False
          
     print(f'{request.session}sdfsdfsdfsdf')
     context={
          'single_blog': single_blog_post,
          'blog_comment': single_blog_page_comment['blog_comment'],
          'total_blog_comment': single_blog_post.totalComments,
          'like_status': like_status
     }
     
     return render(request, 'blog/single_blog_post.html', context)






# Get All comments for a particular blog
def get_single_blog_comment(request, single_blog_post):
     # Gets all the comments
     blog_comment = Comment.objects.filter(blog=single_blog_post)
     
     context = {
          'blog_comment': blog_comment,
     }
     return context


# Create A Blog Comment
# @login_required(login_url='home')
def create_blog_comment(request, single_blog_post):
     if request.method == "POST":
          username = request.POST.get('username')
          comments = request.POST.get('comment')
          
          Comment.objects.create(author = username, comments = comments, blog=single_blog_post)
          
          print ("Comment Created Successfully")
     pass



# Get the Total Number Of Comment Per Blog
def get_total_comment_per_blog(request, single_blog_post):
               
          # After Creating a Comment this Total Comment Number increases
          total_comment_in_blog = Comment.objects.filter(blog=single_blog_post).count()
          
          # print(f'{total_comment_in_blog}')
          
          if total_comment_in_blog == 0:
               single_blog_post.totalComments = 0
               single_blog_post.save()
          else:
               single_blog_post.totalComments = total_comment_in_blog
               single_blog_post.save();
          pass


# Get all Replies for a particular comment from the DataBase
def get_comment_replies(request, single_blog_post):
      # # Get the comment ID
     single_comment_id = request.GET.get("commentId")
     
     if single_comment_id:
          single_comment = Comment.objects.get(id=single_comment_id)
          comment_replies = Reply.objects.filter(comment = single_comment)
          # print(f'{single_comment_id}::::{comment_replies}')
               
          context = {
               'blogPost': single_blog_post,               
               'comments': single_comment,
               'replies': comment_replies
          }
          return context


# Get the total number of replies for a particular comment
def get_total_replies_per_comment(request, single_comment_id):
     replies =  Reply.objects.filter(comment__id=single_comment_id)
     totalReplies = replies.count() 
     print(f'{totalReplies}')
     for reply in replies:
               commentReply = reply.comment
               
               commentReply.totalReplies = totalReplies
               commentReply.save()
     pass


# Create Comment Replies
def blogReply(request):          
     if request.method == 'POST':
          username = request.POST['username']
          comments = request.POST['comment']
          single_comment_id = request.POST['single_comment_id']
          single_comment_blog_id = request.POST['single_comment_blog_id']
          print(f'{single_comment_id}')
          
                         
          Reply.objects.create(author = username, reply=comments, comment_id=single_comment_id)
              # Get the total comment Replies numbr
          
          return redirect('single_blog', id=single_comment_blog_id )
     else:
          return redirect('home')


@login_required(login_url="login")
def create_blog(request):
     profile =  Profile.objects.get(user=request.user)
     print(f'*********** PROFILE IMAGE *******  {profile}')
     if request.method=="POST":
          authorname = request.POST['authorname']
          authorimage = request.POST['authorimage']
          blogtitle = request.POST['blogtitle']
          blogcoverimage = request.FILES['blogcoverimage']
          description = request.POST['description']
          cloudinary.uploader.upload(authorimage)
          cloudinary.uploader.upload(blogcoverimage)
          
          if Blog.objects.filter(title=blogtitle).exists():
               messages.warning(request, 'Blog title already exist')
          else:
               Blog.objects.create(author_name = authorname, author_image=authorimage, title = blogtitle, coverImage = blogcoverimage, description = description )
          
               messages.success(request, "Blog Post Created Successfully")
               return redirect('home')
          
     context={
          'profileImage': profile
     }
     
     return render(request, 'blog/create_blog.html', context)


def handleLikes(request, id):
     blog = Blog.objects.get(id=id)
     response = HttpResponse()
     liked_user = blog.likes.filter(username=request.user).exists()
     if request.method == "POST":
          if request.user.is_authenticated:
               print(f'User Liked: {liked_user}')
               
               if not liked_user:
                    blog.likes.add(request.user)  
                    blog.total_likes += 1
                         
               else:
                    blog.likes.remove(request.user) 
                    blog.total_likes -= 1
          else:
               return redirect('login')
     blog.save()     
     return response
     
               