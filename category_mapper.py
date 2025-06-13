def map_skills_to_category(skills):
    import re

    category_map = {
        "Data Science": [
            "python", "machine learning", "ml", "deep learning", "pandas", "numpy",
            "scikit-learn", "matplotlib", "seaborn", "tensorflow", "pytorch",
            "sql", "data analysis", "r", "statistics", "power bi", "excel", "tableau"
        ],
        "Web Development": [
            "html", "css", "javascript", "js", "react", "angular", "vue", "node.js",
            "express.js", "flask", "django", "bootstrap"
        ],
        "Software Development": [
            "java", "c++", "c", "c#", "kotlin", "swift", "ruby", "go", "php", "typescript"
        ],
        "Cloud Computing": [
            "aws", "azure", "google cloud", "gcp", "cloud", "docker", "kubernetes",
            "linux", "jenkins", "devops", "terraform", "ansible"
        ],
        "Electrical Engineering": [
            "electrical engineering", "circuit design", "pcb design", "microcontroller",
            "arduino", "raspberry pi", "vhdl", "verilog", "embedded systems"
        ],
        "Automation": [
            "plc", "sensors", "control systems", "robotics", "automation", "industrial iot"
        ],
        "UI/UX Design": [
            "ui", "ux", "user experience", "user interface", "figma", "adobe xd", "wireframing",
            "prototyping", "design thinking"
        ],
        "Graphic Design": [
            "photoshop", "illustrator", "graphic design", "canva", "creativity", "branding"
        ],
        "Marketing": [
            "seo", "digital marketing", "email marketing", "social media", "facebook ads",
            "instagram marketing", "adwords", "analytics", "google ads", "advertising"
        ],
        "Content Writing": [
            "content writing", "copywriting", "blogging", "article writing", "proofreading"
        ],
        "Finance": [
            "accounting", "finance", "investment", "banking", "budgeting", "valuation"
        ],
        "Human Resources": [
            "recruitment", "hr", "human resources", "talent acquisition", "payroll", "interviewing"
        ],
        "Soft Skills": [
            "communication", "teamwork", "leadership", "time management", "problem solving",
            "adaptability", "critical thinking", "empathy", "creativity"
        ],
        "Database Management": [
            "sql", "mysql", "mongodb", "oracle", "nosql", "database", "data warehousing", "etl"
        ],
        "Cybersecurity": [
            "cybersecurity", "network security", "ethical hacking", "kali linux", "burpsuite",
            "firewalls", "pen testing", "information security"
        ],
        "Mobile App Development": [
            "android", "ios", "flutter", "react native", "kotlin", "swift", "mobile apps"
        ],
        "Game Development": [
            "unity", "unreal engine", "game development", "cocos", "game design"
        ],
        "Business Analytics": [
            "business analysis", "market research", "excel", "data visualization", "kpi"
        ],
        "Mechanical Engineering": [
            "solidworks", "autocad", "mechanical design", "catia", "ansys", "thermal engineering"
        ]
    }

    matched_categories = set()
    skill_aliases = {s.lower(): cat for cat, keywords in category_map.items() for s in keywords}

    for skill in skills:
        skill_lower = skill.lower().strip()
        # Try exact match first
        if skill_lower in skill_aliases:
            matched_categories.add(skill_aliases[skill_lower])
        else:
            # Try partial fuzzy match
            for keyword, cat in skill_aliases.items():
                if re.search(rf"\b{re.escape(keyword)}\b", skill_lower):
                    matched_categories.add(cat)

    return list(matched_categories) if matched_categories else ["General"]
