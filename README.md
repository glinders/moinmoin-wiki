moinmoin-wiki
=============

Docker image with the Moinmoin wiki engine, uwsgi, nginx and self signed SSL.

You can run this with the following command:
    
    sudo docker run -it -p 443:443 -p 80:80 --name <wikiname> <imagename>
    
Default superuser account is `mmAdmin`. 
It is activated by creating a new user with that name.

The wiki pages (/usr/local/share/moin/data) are exposed as volume, so you can 
take a backup of the system from the host.

You can detach from the container session with `CTRL-P` and then `CTRL-Q`.
