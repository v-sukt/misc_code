##reverseproxy snippet

For apache proxy, to direct the requests to internal service  

```
<VirtualHost *:443>
	#ServerAdmin <webmaster@localhost>
	ServerName server1.example.com
	DocumentRoot "/var/www/html"

	# Logging
	CustomLog "/var/log/apache2/www-access.log" combined
	ErrorLog "/var/log/apache2/www-error.log"
	LogLevel warn

	### Reverse Proxy
   	ProxyPass    "/"      http://localhost:xxxx/ retry=0
  	ProxyPassReverse "/"  http://localhost:xxxx/

	<Proxy *>
		## Auth
		AuthType Basic
		AuthName "Basic-Auth"
		AuthUserFile /path/to/auth/file
		Require valid-user
	</Proxy>
</VirtualHost>
```
