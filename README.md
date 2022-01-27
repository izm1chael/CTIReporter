# CTI Reporter

## Get Started

    git clone https://github.com/izm1chael/CTIReporter.git
    cd CTIReporter
    pip install -r requirments.txt]
    mkdir content
    mkdir users
    cat > /user/users.json <<EOL
    {  
	 "user": {  
	   "active": true,  
	   "authentication_method": "cleartext",  
	   "roles": [],  
       "password": "password",  
       "authenticated": true  
     }  
    }
    flask run
