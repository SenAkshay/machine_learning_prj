## Start Machine Learning Project
A machine Learning project End to End

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)

Creating conda Environment
```
conda create -p <envname> python==3.7 -y

conda activate venv

OR

conda activate <envname>

```

Install liberaries
```
pip install -r requirements.txt

```

Heroku Setup
To setup CI/CD pipeline in heroku we need below 3 items:
1. HEROKU_EMAIL =  akshayxxxxxx@gmail.com
2. HEROKU_API_KEY = a1fcbXXX-bcd2-XXXX-84a3-f64fXXXXX
3. HEROKU_APP_NAME = ml-prj-app

BUILD Docker Image
```
docker build -t <imag_name>:<tagname>

```
>Note: Image name to start with lowercase

To list docker image
```
docker images
```

To run docker image
```
docker run -p 5000:5000 -e PORT=5000 

```

To check docker container
```
docker pa

```

To check latest docker container
```
docker ps -l
```

To stop docker container
```
docker stop <container_id>
```

To kill docker container
```
docker kill <container_id>
```

To create a fresh docker image from existing image
```
docker commit <new_img_name> <container_id_of_parent>
```
