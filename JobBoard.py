class JobBoard:
    def __init__(self):
        self.jobs = []

    def add_job(self, job):
        self.jobs.append(job)

    def display_jobs(self):
        if not self.jobs:
            print("No jobs available.")
        else:
            print("Available Jobs:")
            for job in self.jobs:
                print(job)

    def filter_jobs(self, criteria):
        filtered_jobs = []
        for job in self.jobs:
            if all(getattr(job, attr, None) == value for attr, value in criteria.items()):
                filtered_jobs.append(job)
        return filtered_jobs

    def apply_for_job(self, job, applicant):
        job.applicants.append(applicant)
        print(f"Application submitted for job: {job.title}")

class Job:
    def __init__(self, title, description, location, salary, job_type):
        self.title = title
        self.description = description
        self.location = location
        self.salary = salary
        self.job_type = job_type
        self.applicants = []

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nLocation: {self.location}\nSalary: {self.salary}\nJob Type: {self.job_type}"

if __name__ == "__main__":
    job_board = JobBoard()
    job_board.add_job(Job("Software Engineer", "Develop software applications", "Remote", 100000, "Full-time"))
    job_board.add_job(Job("Data Analyst", "Analyze data to provide insights", "New York", 90000, "Full-time"))
    job_board.add_job(Job("Marketing Manager", "Develop marketing strategies", "San Francisco", 95000, "Part-time"))

    print("All Jobs:")
    job_board.display_jobs()

    print("\nFiltering Jobs by Location:")
    filtered_jobs = job_board.filter_jobs({"location": "Remote"})
    for job in filtered_jobs:
        print(job)

    print("\nApplying for a Job:")
    selected_job = job_board.jobs[0]
    job_board.apply_for_job(selected_job, "John Doe")
    print(f"Applicants for {selected_job.title}: {selected_job.applicants}")
