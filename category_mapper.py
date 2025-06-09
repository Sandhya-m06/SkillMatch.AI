def map_skills_to_category(skills):
    category_map = {
        # Data Science / Analytics
        "python": "Data Science",
        "machine learning": "Data Science",
        "deep learning": "Data Science",
        "pandas": "Data Science",
        "numpy": "Data Science",
        "tensorflow": "Data Science",
        "pytorch": "Data Science",
        "sql": "Data Science",
        "excel": "Data Science",
        "data analysis": "Data Science",
        "power bi": "Data Science",
        "statistics": "Data Science",
        "r": "Data Science",

        # Web Development
        "html": "Web Development",
        "css": "Web Development",
        "javascript": "Web Development",
        "react": "Web Development",
        "node.js": "Web Development",
        "flask": "Web Development",
        "django": "Web Development",
        "angular": "Web Development",
        "vue": "Web Development",

        # Software Development / Programming Languages
        "java": "Software Development",
        "c++": "Software Development",
        "c": "Software Development",
        "c#": "Software Development",
        "ruby": "Software Development",
        "swift": "Software Development",
        "kotlin": "Software Development",
        "php": "Software Development",

        # Cloud Computing / DevOps / IT
        "aws": "Cloud Computing",
        "azure": "Cloud Computing",
        "google cloud": "Cloud Computing",
        "linux": "Cloud Computing",
        "docker": "Cloud Computing",
        "kubernetes": "Cloud Computing",
        "devops": "Cloud Computing",
        "networking": "Cloud Computing",

        # Electrical / Electronics / Automation
        "electrical engineering": "Electrical Engineering",
        "circuit design": "Electrical Engineering",
        "embedded systems": "Electrical Engineering",
        "microcontroller": "Electrical Engineering",
        "pcb design": "Electrical Engineering",
        "automation": "Automation",
        "robotics": "Automation",
        "control systems": "Automation",
        "sensors": "Automation",
        "plc": "Automation",

        # Design / Creative
        "figma": "UI/UX Design",
        "adobe xd": "UI/UX Design",
        "photoshop": "Graphic Design",
        "illustrator": "Graphic Design",
        "ui/ux": "UI/UX Design",
        "user experience": "UI/UX Design",
        "user interface": "UI/UX Design",
        "graphic design": "Graphic Design",

        # Marketing / Content
        "seo": "Marketing",
        "digital marketing": "Marketing",
        "social media": "Marketing",
        "content writing": "Content Writing",
        "copywriting": "Content Writing",
        "blogging": "Content Writing",
        "advertising": "Marketing",

        # Finance / Accounting
        "accounting": "Finance",
        "finance": "Finance",
        "investment": "Finance",
        "banking": "Finance",
        "budgeting": "Finance",
        "excel": "Finance",

        # Human Resources / Soft Skills
        "recruitment": "Human Resources",
        "hr": "Human Resources",
        "human resources": "Human Resources",
        "payroll": "Human Resources",
        "communication": "Soft Skills",
        "teamwork": "Soft Skills",
        "leadership": "Soft Skills",
        "time management": "Soft Skills",
        "problem solving": "Soft Skills",
        "adaptability": "Soft Skills",
        "critical thinking": "Soft Skills",

        # Other technical skills
        "sql": "Database Management",
        "mongodb": "Database Management",
        "data warehousing": "Database Management",
        "etl": "Database Management",
    }

    matched = set()
    for skill in skills:
        skill_lower = skill.lower()
        if skill_lower in category_map:
            matched.add(category_map[skill_lower])

    # If no categories matched, default to General
    return list(matched) if matched else ["General"]
