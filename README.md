
# CTI Reporter

### Description
CTI Reporter is a small flask application designed to aid in Cyber Threat Intelligence reporting. It has been designed as an editor and organizer of markdown files. It offers the ability to tag various fields within the report and indexes and searches based on those criteria.

### Current Features
	- Regex Search
	- Filter by assigned tabs of indicators of compromise
	- Markdown Editor
	- Populated Intellegence Cards
	- Index by fields


### Road Map

	 - RBAC - Build out a robust role based accese system
	 - Export as PDF
	 - Schedule email of reports
	 - Admin Section

## Get Started

    git clone https://github.com/izm1chael/CTIReporter.git
    cd CTIReporter
    pip install -r requirments.txt
    mkdir content
    mkdir user
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
