from fpdf import FPDF

class AssignmentPDF(FPDF):
    def __init__(self):
        super().__init__()
        # Use built-in fonts for portability (Helvetica as substitute for Arial)
        self.set_auto_page_break(auto=True, margin=15)
        self.set_font('Helvetica', '', 12)

    def header(self):
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, 'UNIT 4 - Assignment 4: Questions & Answers', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_question(self, idx, marks, question, answer):
        # Question header
        self.set_font('Helvetica', 'B', 12)
        self.multi_cell(0, 8, f'{idx}. ({marks} Marks) {question}')
        self.ln(2)
        # Answer body
        self.set_font('Helvetica', '', 11)
        self.multi_cell(0, 6, answer)
        self.ln(8)

# List of questions and answers
tab = [
    # 5 Marks Q&A
    (1, 5,
     "What is LinkedIn, and what role does it play in shaping professional identities and networking opportunities?",
     "LinkedIn is a global professional networking platform that enables individuals to showcase their career history, skills, and accomplishments. It serves as a digital resume and portfolio, helping users build and manage their professional identity online. By connecting with colleagues, mentors, and industry leaders, LinkedIn facilitates networking opportunities, job searches, and knowledge sharing across diverse fields."),

    (2, 5,
     "Discuss the significance of LinkedIn in establishing a credible and professional online presence.",
     "A complete LinkedIn profile with a professional photo, detailed experience, and endorsements enhances credibility and visibility. Recruiters and peers often evaluate candidates based on their LinkedIn pages; a well‑crafted presence signals competence and attention to detail. Additionally, publishing articles or sharing industry insights positions individuals as thought leaders and builds trust within their network."),

    (3, 5,
     "How does showcasing skills and achievements on LinkedIn contribute to creating a strong professional image? Provide examples of effective ways to highlight key accomplishments.",
     "Listing skills and receiving endorsements validates one’s expertise to viewers. Adding project descriptions, certification badges, and multimedia samples (e.g., slide decks, code repositories) brings tangible proof of ability. For example, embedding a link to a published research paper or a cloud‑deployed application demonstrates practical accomplishments and enhances the professional image."),

    # 10 Marks Q&A
    (4, 10,
     "Explain the key components of a LinkedIn page as discussed. How do these components contribute to creating a comprehensive professional profile?",
     "A LinkedIn page comprises Profile Photo, Headline, About section, Experience, Education, Skills, and Recommendations. The Photo and Headline immediately create a first impression. The About section provides a concise narrative of the user’s background and career goals. Detailed Experience and Education chronicle one’s journey and qualifications. Skills and Recommendations serve as social proof, while additional sections like Certifications and Projects enrich the profile with relevant evidence of expertise."),

    (5, 10,
     "In the process of setting up a LinkedIn profile, discuss the essential steps involved in creating an effective LinkedIn profile, considering both content and presentation.",
     "Start by uploading a high‑resolution, professional headshot and writing a keyword‑optimized headline. Craft a compelling About summary (3–5 sentences) that outlines your value proposition. List all relevant work and academic experiences, focusing on achievements rather than duties. Add 5–10 key skills and seek endorsements from colleagues. Complete optional sections—Certifications, Volunteer Work, Projects—to showcase breadth. Finally, maintain consistent formatting and use bullet points for readability."),

    (6, 10,
     "Describe the process of LinkedIn optimization. How can individuals ensure that their profiles are optimized to attract relevant connections and opportunities?",
     "Optimization begins with identifying industry‑specific keywords and incorporating them in the Headline, About, and Experience sections. Customize the LinkedIn URL for professionalism. Regularly publish or share articles, updates, and insights to increase visibility. Engage with others by commenting on posts and joining relevant Groups. Analyze profile views and search appearances via LinkedIn analytics, and iteratively refine content based on performance metrics."),

    # 20 Marks Q&A
    (7, 20,
     "Building a personal brand on LinkedIn involves several steps. Explain the concept of personal branding and its relevance in the digital age. How can individuals effectively showcase their expertise and create a distinct brand identity on LinkedIn?",
     "Personal branding is the deliberate process of defining and promoting what you stand for, your unique skills, values, and experiences. In the digital age, where first impressions occur online, a strong personal brand differentiates professionals in a crowded marketplace. On LinkedIn, individuals can craft a consistent narrative across their Headline, About, and Experience sections that highlights niche expertise. Publishing thought leadership content (articles, white papers) and participating in industry discussions reinforces credibility. Using a cohesive visual style—professional banner image and headshot—further solidifies brand recognition. Collecting endorsements and recommendations from respected peers provides social proof, rounding out a distinct and trustworthy brand identity."),

    (8, 20,
     "The importance of practice in utilizing LinkedIn effectively was highlighted. Discuss the significance of hands-on practice in mastering the art of networking and branding on LinkedIn. Provide examples of how practice sessions can enhance users' proficiency in creating and managing their profiles.",
     "Hands‑on practice empowers users to explore LinkedIn’s features and refine their approach. For example, conducting mock networking outreach allows one to test different message styles and measure response rates. Practice drafting posts or articles in a private document helps optimize tone and structure before publishing. Running profile audits—having peers review and provide feedback—mirrors real‑world critique and accelerates improvement. Regularly simulating search queries with target keywords teaches how to align one’s profile language with recruiter expectations. Through iterative practice, users gain confidence and develop an authentic online presence that resonates with their professional audience."),

    (9, 20,
     "Reflecting on the content covered, analyze the role of LinkedIn in shaping professional identities and facilitating career growth. How can the knowledge and skills acquired be applied in real-world scenarios to leverage LinkedIn as a powerful tool for networking and personal branding?",
     "LinkedIn consolidates multiple facets of one's career—resume, portfolio, and network—into a single platform, making it central to modern professional identity. Skills in profile optimization and content creation translate directly to higher visibility among industry peers and recruiters. In practice, a user might leverage LinkedIn to research and connect with alumni before attending a conference, then reference shared interests to build rapport. Regularly sharing project updates or blog posts demonstrates ongoing development to hiring managers. By applying analytics insights, professionals can focus on high‑impact activities—such as targeted outreach or group participation—that drive real‑world opportunities."),

    (10, 20,
     "In today's competitive job market, LinkedIn has become a crucial platform for professionals to network and showcase their skills. Discuss the evolving role of LinkedIn in modern career development and its impact on shaping professional identities. Provide examples of professionals who have successfully utilized LinkedIn to expand their professional opportunities and establish themselves in their respective industries.",
     "Beyond job listings, LinkedIn now functions as a dynamic marketplace of ideas and opportunities. Thought leaders publish long-form articles that influence industry dialogue. For instance, a data scientist may share machine‑learning tutorials, attracting collaboration offers and speaking engagements. Entrepreneurs often use LinkedIn to validate business ideas via surveys and to secure investor interest through their professional footprint. Recruiters increasingly rely on LinkedIn’s Recruiter tool, emphasizing the need for proactive profile management. As professionals across fields—from marketing to engineering—leverage rich media posts, live videos, and newsletters, LinkedIn continues to redefine career development and personal branding in the digital era."),
]

# Generate the PDF
if __name__ == '__main__':
    pdf = AssignmentPDF()
    pdf.add_page()
    for q in tab:
        pdf.add_question(*q)
    pdf.output('Unit4_Assignment4_Answers.pdf')
    print('PDF generated successfully: Unit4_Assignment4_Answers.pdf')