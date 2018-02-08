### Lesson 0 - The Setup
#### introduction
- Install [Python 3.6](https://www.python.org/downloads/release/python-364/)
- Install [PyCharm Community Edition IDE](https://www.jetbrains.com/pycharm/download/) - strongly recommended
- Install [git download](https://git-scm.com/downloads)
- Introductory YouTube video for git [1](https://www.youtube.com/watch?v=SWYqp7iY_Tc) [2](https://www.youtube.com/watch?v=FQsBmnZvBdc)
- Install some cool python packages: run command in cmd/terminal `pip install ipython pytest ipdb`

#### Practice
1. Install Python and PyCharm.
1. Fork the repository (check out [Forking Projects](https://guides.github.com/activities/forking/)
1. Git clone your fork (use the address from GitHub).
1. Create your branch `git branch first_name.last_name/lesson_00_the_setup`.
1. Check the branch out `git checkout first_name.last_name/lesson_00_the_setup`.
1. (A shorter version for the above is `git checkout -b ...`.
1. Create your directory in  /students/(surname).(name),
1. Copy `lesson_00_the_setup` to your directory,
1. Make example commits,
    1. Add the file to git staging area: `git add hello_world.py`.
    1. `git commit` and enter a reasonable commit message.
    1. Copy content of `importable_module.py` to `hello_world.py`.
    1. Add `hello_world.py` to the staging area again.
    1. Commit with a pretty commit message.
1. Push the branch to your fork `git push origin first_name.last_name/lesson_00_the_setup`
1. Go to the original repository and create a pull request from your branch in the fork to the original.
1. Remember to check out master branch before you proceed to the next lesson.
