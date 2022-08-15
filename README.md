## qquiet

### Dev setup with debugger
docker-compose up -d
docker attach qquiet_web_1




## Common Getting Started Commands
### Docker
docker-compose build // adding new dependencies
docker-compose up
docker-compose down
docker container exec -it <container_id>  /bin/bash

### with PDB
docker-compose up -d
docker attach qquiet_web_1
//docker attach <project>_<djangocontainername>_1

-- for breakpoint
import pdb; pdb.set_trace()

### Migrations 
python manage.py makemigrations qquiet
python manage.py sqlmigrate qquiet 0001
python manage.py migrate

### Admin
python manage.py createsuperuser
http://localhost:8000/admin/

### Console
python manage.py shell
from qquiet.models import *
Location.objects.get(id=1)

#### Create object
l = Location(address='240 E 76th ST Apt 2F NY, NY 10021', created_at=datetime.now())
l.save


#### TODO
--basic get endpoint and api docs--
setup api endpoint to POST audio files 
setup boto3 to read/write S3 
setup api keys for api 





##### CUT
around debugging
-- in file
-- from django.http import HttpResponse






