FROM ubuntu
RUN useradd -m newuser && passwd -d newuser
VOLUME /ex21_vol
COPY  /home/parallels/Desktop/git/containers/docker/ex19.sh /ex21_vol/ex19.sh
RUN chown newuser /ex21_vol/ex19.sh 
