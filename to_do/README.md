Requirments for django_test project (djtp)
==========================================

### Project Directory Structure:

<pre>
 /some/path/to/django_test/
    logs/ - place any logs here (git ignored)
    djtp_virutalenv/ - virtualenv should be installed here (git ignored)
    source/ - django project lives here
    socket/ - if you are using gunicorn, place its socketfile here (git ignored)
    docs/ - let people know the good things you have done
    dbs/ - put your local databases here (git ignored)
</pre>

### Python OS Packages:
* pip
* virtualenv

### Virtualenv Packages:
* django
* pep8
* pylint

> requirments.txt lives in docs/

### Project Dependancies:
https://github.com/twbs/bootstrap/releases/download/v3.3.2/bootstrap-3.3.2-dist.zip

> extract into 'source/static'

