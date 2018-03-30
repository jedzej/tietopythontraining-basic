### Lesson 0 - The Setup
#### introduction

- Install [Python 3.6](https://www.python.org/downloads/release/python-364/),
- Install [PyCharm Community Edition IDE](https://www.jetbrains.com/pycharm/download/) - strongly recommended,
- Install [git vesion control](https://git-scm.com/downloads),
- Get to know git:
    - [What? Why do I need version control?](https://git-scm.com/videos) -- optional introductory motivation video
    - [How do I use version control?](https://www.youtube.com/watch?v=SWYqp7iY_Tc)
    - [How do I make a pull request on GitHub?](https://www.youtube.com/watch?v=FQsBmnZvBdc)
- Install some cool python packages: run command in cmd/terminal `pip install ipython pytest ipdb`


#### Practice
1. Install Python and PyCharm.
1. Fork the repository (check out [Forking Projects](https://guides.github.com/activities/forking/))
1. Git clone your fork (use the address from GitHub), cd into `tietopythontraining-basic`.
1. Create your branch `git branch (reviewer_login)/lesson_00_the_setup`.
1. Check the branch out `git checkout (reviewer_login)/lesson_00_the_setup`.
1. (A shorter version for the above is `git checkout -b ...`.
1. Create your directory in  /students/(last_name)_(first_name),
1. Copy `lesson_00_the_setup` to your directory,
1. Make example commits,
    1. Add the file to git staging area: `git add hello_world.py`.
    1. `git commit` and enter a reasonable commit message.
    1. Copy content of `importable_module.py` to `hello_world.py`.
    1. Add `hello_world.py` to the staging area again.
    1. Commit with a pretty commit message.
1. Push the branch to your fork `git push origin (reviewer_login)/lesson_00_the_setup`
1. Go to the original repository and create a pull request from your branch in the fork to master branch in base(original repo).
1. Notify your reviewer using @mention when PR is ready to review ([check this out](https://github.com/blog/821-mention-somebody-they-re-notified))
1. Remember to check out master branch before you proceed to the next lesson. (check out [Git reference materials for details](https://github.com/jedzej/tietopythontraining-basic#reference-materials))


##### Expected problems
If you encounter problems with some pre-requisites, we didn't talk
about, don't hesitate to ask. We will try to direct you (at least give
you some Google search keywords). Some example issues:
1. Problems with command line? Quick intro needed?
1. Will git on Windows open vim for editing?
1. Is there a usable shell on Windows?
1. PyCharm is intimidating? Try VS Code.
