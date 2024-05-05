import unittest
from JobBoard import Job, JobBoard

class TestJobBoard(unittest.TestCase):
    def setUp(self):
        self.job_board = JobBoard()
        self.job_board.add_job(Job("Software Engineer", "Develop software applications", "Remote", 100000, "Full-time"))
        self.job_board.add_job(Job("Data Analyst", "Analyze data to provide insights", "New York", 90000, "Full-time"))
        self.job_board.add_job(Job("Marketing Manager", "Develop marketing strategies", "San Francisco", 95000, "Part-time"))

    def test_add_job(self):
        self.assertEqual(len(self.job_board.jobs), 3)

    def test_filter_jobs(self):
        filtered_jobs = self.job_board.filter_jobs({"location": "Remote"})
        self.assertEqual(len(filtered_jobs), 1)
        self.assertEqual(filtered_jobs[0].title, "Software Engineer")

    def test_apply_for_job(self):
        selected_job = self.job_board.jobs[0]
        self.job_board.apply_for_job(selected_job, "John Doe")
        self.assertEqual(len(selected_job.applicants), 1)
        self.assertEqual(selected_job.applicants[0], "John Doe")

if __name__ == "__main__":
    unittest.main()


