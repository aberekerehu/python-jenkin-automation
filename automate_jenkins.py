import jenkins
import json
import os

def create_jenkins_server():
    host = "http://192.168.13.153:8080"
    username = "akerehu"  # Jenkins username here
    password = "11f107144f230b890216d73144ccf4cd8d"  # Jenkins user password / API token here
    server = jenkins.Jenkins(host, username=username, password=password)
    return server

def print_jenkins_user_and_version(server):
    user = server.get_whoami()
    version = server.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))

def create_blank_job(server, job_name):
    server.create_job(job_name, jenkins.EMPTY_CONFIG_XML)
    print(f"Created job: {job_name}")

def create_preconfigured_job(server, job_name, config_xml):
    server.create_job(job_name, config_xml)
    print(f"Created job: {job_name}")

def view_jobs(server):
    jobs = server.get_jobs()
    print("Jobs:")
    for job in jobs:
        print(job['name'])
def copy_job(server):
    server.copy_job('job2', 'job4')

def update_job(server):
    updated_job_3 = open("job_3_updated.xml", mode='r', encoding='utf-8').read()
    server.reconfig_job('job3', updated_job_3)

def disable_job(server):
    server.disable_job('sample_job')
# Run a build and get build number and more info
def build_job(server):
    server.build_job('job3')
    last_build_number = server.get_job_info('job3')['lastCompletedBuild']['number']
    print("Build Number", last_build_number)
    build_info = server.get_build_info('job3', last_build_number)
    print("build info", build_info)

def delete_job(server):
     server.delete_job('sample_job')

def create_view(server):
    view_config = open("jobs_view.xml", mode='r', encoding='utf-8').read()
    server.create_view("Job List", view_config)

def get_list_of_views(server):
    views = server.get_views()
    print(views)

def update_view(server):
    updated_view_config = open("jobs_view_updated.xml", mode='r', encoding='utf-8').read()
    server.reconfig_view("Job List", updated_view_config)

def delete_view(server):
    server.delete_view("Job List")

def main():
    jenkins_server = create_jenkins_server()
    print_jenkins_user_and_version(jenkins_server)

    # Uncomment the desired function to test
    

    # Create deployment jobs
    create_blank_job(jenkins_server, "job1")
    
    job2_xml = open("python-flsk-docker-job.xml", mode='r', encoding='utf-8').read()
    create_preconfigured_job(jenkins_server, "job2", job2_xml)

   
    # View jobs
    view_jobs(jenkins_server)

    #copy Job
    #copy_job(jenkins_server)

    #update Job
    #update_job(jenkins_server)

    #disable Job
    #disable_job(jenkins_server)

    #delete Job
    #delete_job(jenkins_server)

    



if __name__ == "__main__":
    main()

















