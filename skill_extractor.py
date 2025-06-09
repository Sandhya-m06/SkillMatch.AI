def extract_skills(text):
    known_skills = [
        # Data Science / Analytics
        "python", "machine learning", "deep learning", "pandas", "numpy",
        "tensorflow", "pytorch", "sql", "excel", "data analysis", "power bi",
        "statistics", "r",

        # Web Development
        "html", "css", "javascript", "react", "node.js", "flask", "django",
        "angular", "vue",

        # Software Development
        "java", "c++", "c", "c#", "ruby", "swift", "kotlin", "php",

        # Cloud Computing / DevOps
        "aws", "azure", "google cloud", "linux", "docker", "kubernetes",
        "devops", "networking",

        # Electrical / Automation
        "electrical engineering", "circuit design", "embedded systems",
        "microcontroller", "pcb design", "automation", "robotics",
        "control systems", "sensors", "plc",

        # Design
        "figma", "adobe xd", "photoshop", "illustrator", "ui/ux",
        "user experience", "user interface", "graphic design",

        # Marketing / Content
        "seo", "digital marketing", "social media", "content writing",
        "copywriting", "blogging", "advertising",

        # Finance
        "accounting", "finance", "investment", "banking", "budgeting",

        # Human Resources / Soft Skills
        "recruitment", "hr", "human resources", "payroll", "communication",
        "teamwork", "leadership", "time management", "problem solving",
        "adaptability", "critical thinking",

        # Other technical
        "mongodb", "data warehousing", "etl"
    ]
    text = text.lower()
    extracted = []
    for skill in known_skills:
        if skill in text:
            extracted.append(skill)
    return extracted
