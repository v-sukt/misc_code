## Rewrite snippet
add following snippet to rewrite the request coming on http to https port

```        RewriteEngine On
        RewriteCond %{HTTPS} !=on
        RewriteRule ^/?(.*) https://%{SERVER_NAME}/$1 [R,L]
```

this must be part of the default apache configuration. default in the sense - one that is referred for port 80 first. The order is as per teh alphabetic names 
000-default       <- will be loaded first
001-default
