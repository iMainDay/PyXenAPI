## Download library 
At the moment, the library can be installed in the following ways:

=== "From Github"
	```bash
	pip install -U https://github.com/iMainDay/PyXenApi/archive/master.zip
	```
=== "PyPi"
	```bash
	pip install PyXenApi
	```

## Create instance 
```py linenums="1"
from PyXenApi import XenForoAPI

xf = XenForoAPI('myApiToken', 'https://mydomain.com/api/')
```

!!! warning
	The domain parameter must be passed as a **link**, including **http://** or **https://** and ending with the api endpoint. 
	Example: `https://xenforo.com/api/`