import os
import requests
from dotenv import load_dotenv

class AIMEngTool:
    def __init__(self):
        load_dotenv()
        self.api_url = (
            "https://streamer.oit.duke.edu/curriculum/courses/subject/"
            "AIPI%20-%20AI%20for%20Product%20Innovation"
        )
        self.token = os.getenv("DUKE_API_KEY")

    def run(self, query: str) -> str:
        try:
            response = requests.get(f"{self.api_url}?access_token={self.token}")
            response.raise_for_status()
            data = response.json()

            courses = data["ssr_get_courses_resp"]["course_search_result"]["subjects"]["subject"]["course_summaries"]["course_summary"]
            course_list = []

            for course in courses:
                title = course["course_title_long"]
                catalog = course["catalog_nbr"].strip()
                semester = course.get("ssr_crse_typoff_cd_lov_descr", "N/A")
                course_list.append(f"- {catalog}: {title} ({semester})")

            return "**AIPI Courses at Duke:**\n" + "\n".join(course_list)

        except Exception as e:
            return f"Error fetching AIPI course data: {str(e)}"
