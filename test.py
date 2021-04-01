from pathlib import Path
import spacy
from spacy.scorer import Scorer
from spacy.training import Example


def evaluate(ner_model, examples):
    scorer = Scorer()
    for sents, ents in examples:
        doc = ner_model.make_doc(sents)
        example = Example.from_dict(doc, {"entities": ents['entities']})
        print(scorer.score(example))


output_dir = Path('pretrained_model')
print("Loading from", output_dir)
nlp_blanked = spacy.load(output_dir)
doc = nlp_blanked("""FEI PENG




GRAPHIC DESIGNER /
Fei Peng Faye0315@gmail.com (415)425-7456
feipengdesign.com

OBJECTIVE /
I�m seeking a position as a junior designer that focuses on visual design, branding design and UI/UX design in a company where I can utilize my skills and contribute to a creative design team.





EDUCATION / 
MFA
Academy of Art University, San Francisco
Graphic Design and Digital Media

BFA
Hubei University of Technology, China Computer Art Design

EXPERIENCE /
BLUE WANDER
Helping BlueWander with the design of its product, website, and communication materials.
www.bluewander.life
Position: Graphic Designer Consultant / June 2018 - Currently

ROBOT GYMS
Created a brand system for this company including a logo system, advertising brochures and class lists. Character design, layout design and organize published books.
robotgyms.com
Position: Graphic Designer (Freelance) / Sep 2017 - Currently

PAPER CULTURE
Review overall design aesthetic including colors, typography and
layout - making suggestions and changes where appropriate. Review customer files for typographical errors, grammar, style suggestions, and missing information. Provide feedback directly to customers via email
paperculture.com
Position: Associate Designer / Apr 2018� July 2018

SKILLS /
Adobe Creative Cloud, Google Suite

LANGUAGES /
English, Mandarin Chinese

INTERESTS /
Traveling, Play Traditional Music Instrument, Skiing

REFERENCES /
Furnished upon request.
QIAN (JENNY) WANG 
 Los Angeles, CA, 90057 Phone: 925-738-8098 E-mail: qwang504@marshall.usc.edu 
 EDUCATION 
 University of Southern California, Marshall School of Business - Los Angeles, CA May 2019 - May 2020 
 Master of Science, Marketing - Analytics track (STEM) 
 Program Student Council - Social Chair, organize student events and activities 

 Hong Kong University of Science & Technology - Hong Kong SAR Aug 2013 - Nov 2014 
 Master of Science, International Management, collocated with CEMS 
 University of Sydney (Abroad) - Sydney, Australia Feb 2014 - Jun 2014 

 Donghua University - Shanghai, China Sep 2009 - Jun 2013 
 Bachelor of Economics, Finance 
 Montclair State University (Abroad) - New Jersey, NJ Feb 2011 - Aug 2011 

 EXPERIENCE 
 Segway, Inc - Los Angeles, CA 2019 
 Product Management Intern 
   Work with the Product Management team with weekly and quarterly duties such as market analysis, competitive   analysis, technical analysis, and forecasting to launch 10 new products in the second quarter. 
   Partner with the Marketing team to develop and drive go-to-market through various channels and generate insights   on products that lead to breakthrough messaging, accelerated service adoption, and differentiated GTM tactics. 

 Udacity, Inc - Shanghai, China 2018 - 2019 
 Product Marketing Manager 
   Performed data-driven marketing strategy and detailed analysis of gaps and opportunities to achieve the revenue   targets and enrollments of School of Data. 
   Built up new dashboards on Google Analytics and Chartio (SQL) to monitor marketing performance. 
   Designed and led 'Double 11 campaign' and optimized paid acquisition channels and operation process throughout   the campaign. Achieved 50% YOY growth. 
   Planned, executed and optimized paid and non-paid acquisition campaigns across multiple channels - including SEM, 
 PPC, KOL, content marketing, email marketing, etc. 

 DotC United Group - Shanghai, China 2016 - 2018 
 Marketing Manager/Growth Hacker 
   Launched the bike-sharing service in more than 10 cities in Europe, Asia and Australia by working with government   offices to acquire appropriate permits, working with tech teams on localizing App payment methods and languages,   hiring and training local teams, and tracking work flow with local teams to measure projected KPIs. 
   Collected and analyzed data from data Dashboard and performed in-depth analysis of marketing funnels, and   improved 30% of the total conversion rate and achieve 120% of the total project revenue and targets. 
   Communicated with cross-functional teams to ensure business and tech team alignments. 

 Didi Chuxing Group - Hong Kong SAR 2014 - 2016 
 Assistant Marketing Manager 
   Collected and analyzed data from marketing promotions and campaigns to provided analytics and data support   proposals for future growth, established the company as the No.1 ride-sharing service in Hong Kong after 6 months. 
   Liaised closely with technical personnel to ensure mutual understanding of data selection and analysis. 
   Excelled by earning promotion within 3 months of joining the company. 

 Joinjoy Co. - Sydney, Australia 2014 
 Co-founder & CMO 
   Arranged company events and outdoor activities targeting international students to help adapt to local society. 
   Increased over 5000 members and cooperated with more than 50 client partners within 6 months. 

 SKILLS AND INTERESTS 
 Certifications: 
 Udacity - Data Analyst Nano Degree Apr 2019 
 Udacity - Business Analytics Nano Degree Sept 2019 
 Computer skills: SQL, Python, R, Tableau, Google Analytics, SPSS, SAS, JMP, Stata, Microsoft Office 
 Volunteer: Stepping Stone, Teach English to underprivileged children in migrant schools in Shanghai from 2016 to 2019. 
 Language: Fluent English (IELTS:7.5/9; GMAT:720/800), Fluent Mandarin and Cantonese, Basic Korean & Spanish 
Hai Ngo 
Santa Barbara, CA 93109 | (805) 886-7249 | nthai2008@gmail.com | linkedin.com/in/hai-ngo-09 
PROFESSIONAL SUMMARY 
Business Advisor and former Business Owner with over 5 years of experience in retail and distribution, especially e-commerce. Success at developing strategic plans to meet business objectives and drive growth. Advanced knowledge of strategic planning, B2B and B2C sales and new business development. Expertise in marketing, product sourcing, decision making, problem solving and contract negotiation. Excellent ability to manage and work in a diverse and collaborative environment. 

WORK HISTORY 
Business Advisor (Remote) Aug. 2017 - Current  

Lockhartz Ho Chi Minh, Vietnam  
  Advise and assist business owner remotely via phone and email on how to work with suppliers, resolve issues with quality control and fulfillment, create listings, and run promotions that generate leads 
  Utilize strong interpersonal communication skills to connect with SMBs and C-Suites in South East Asia to increase sales monthly by at least 10% 
  Use inbound marketing and outbound prospecting skills to find customers with highest buying potential and lower customer acquisition cost 
  Liaise and collaborate with client teams to identify potential risks and pain points in deliverables and services 
Co-owner/Executive Manager Aug. 2016 - July 2017  
Sique Deals Oceanside, CA  
  Overlooked all operations including inventory control, supply chain, logistics, customer service, dispute resolution, recruiting, training and evaluating employees 
  Evaluated suppliers to assess quality, timeliness and compliance of deliveries, reduce cost of goods sold (COGS) and maximize business operational efficiency 
  Managed key accounts, including developing sales presentations and promotion initiatives to drive product sales and increase brand awareness 
  Devised and deployed sales and marketing tactics to drive strategic growth and support achievement of revenue goals, with sales exceeding $1.1 million annually, compound monthly growth rate was 47.08% 
  Customer feedback yielded 99.7% satisfaction with product, shipping and customer service 
Co-owner/Executive Manager Jan. 2015 - July 2016  
Sales Shock Chino, CA  
  Developed successful marketing and business plans that increased web traffic by 30% monthly 
  Negotiated agreements and contracted with suppliers from China and Vietnam to obtain best rates 
  Implemented pricing, shipping, return policies and established budgets that helped exceed sales goals 
  Conducted target market research to scope out industry competition and identify advantageous trends 
  Exceeded revenue goals with sales surpassing $500,000 annually 
  Customer feedback yielded 99.6% satisfaction with product, shipping and customer service 
EDUCATION 
Bachelor of Arts in Marketing  Mar. 2020  

Antioch University Santa Barbara, CA  
Associate of Arts in Business Administration  June 2018  
Santa Barbara City College Santa Barbara, CA  
Double Majored in Engineering 
Coursework in Electrical Engineering  2017  
California Polytechnic State University-San Luis Obispo San Luis Obispo, CA  
SKILLS 
          Microsoft Office (Word, Excel, PowerPoint, Outlook) 

          Salesforce, Zendesk, SaaS and CRM softwares 
          QuickBooks, KPIs, Google Analytics and G-Suite 
          Interpersonal Communication 
          Time Management and Organizational Skills  
          Customer Satisfaction 
          Inbound Marketing and Outside Sales 
        	  Analytical and Quantitative Skills 
          Presentation Skills 
          Relationship Building 
          Leadership Skills 
          Multi-tasking 
          Detail-oriented 
          Excellent verbal and written communication skills 


 Nancy Zhu 
 4300 W Sarah St. Burbank, CA, 91505 � (818) 468-6629� nancyzhu1996@gmail.com 
 EDUCATION 

 Pepperdine Graziadio Business School Malibu, US 
 Master in Applied Finance, GPA 3.30/4.0 Aug, 2019 

 University of Liverpool Liverpool, UK 
 BA in Accounting, GPA 3.52/4.0 Jul 2018 
 PROFESSIONAL EXPERIENCE 

 Dominieren Corporation West Hollywood, CA 
 Financial Analyst Apr - Aug 2019 
   Collaborated with multiple departments and developed sales & budget reports with advanced Excel forecasting tool. 
   Researched over millions of U.S residents' wage levels in five U.S. metropolitan cities and estimated the number of   customer basements with Pivot Table and Index-match function. 
   Achieved Tableau visualization to reflect influential revenue factors and allocate resources for efficiency improvement. 
 GapcapitalPartner Beverly Hills, CA 
 Venture Capital Analyst Jan - Mar 2019 
   Built financial models to develop financial statements database for start-up companies. 
   Analyzed profitability and risk using Excel, including NPV, IRR, Payback Period and Sensitivity Analysis. 
   Constructed revenue statistical forecast and regression analysis with advanced Excel formulas (Vlookup, Hlookup, Offset). 
   Predicted the financial feasibility of companies. 
 P&G Company Shanghai, China 
 Financial Analyst Intern Jun-Sep. 2017 
   Utilized NetSuite Oracle to report monthly sales and shipment to distributors. 
   Closed monthly A/R and shipment inventory report with Blackline. 
   Visualized trend of month-end statistical journal entries with Tableau Server and Power Pivot. 
 PROJECT EXPERIENCE 

 ACG M&A Analysis Competition, Pepperdine University Nov. - Dec 2018 
   Calculated EV and Equity by using DCF Model, Comparable Companies Analysis Model, and Precedent Companies 
 Analysis Model. 
   Assessed the merged feasibility by building the Leveraged Buyout Model and calculating the cash return ratio and IRR. 
   Built the pro forma after the acquisition and combined the merged EPS and stand-along EPS. 
 LBO Case Study, Pepperdine University Jan - May 2017 
   Built the future 5 years pro forma for Pepperco Inc. based on the available and the estimated data. 
   Compare the acquisition Enterprise Value and Exit Enterprise Value and Gave the investment recommendation by   calculating cash return and ROI. 
   Built the sensitivity analysis metrics using Excel between revenue growth ratio and EBITDA/Revenue. 
 ADDITIONAL INFOR 
 Language Skills: Mandarin, English and Spanish 
 Technical Skills: Excel, R programming, Tableau, VBA, Macro 
 Interests: High Strength Aerobic Activity 
""")
print("Entities", [(ent.text, ent.label_) for ent in doc.ents])

