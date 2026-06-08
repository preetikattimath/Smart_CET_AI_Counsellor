# data/colleges.py

COLLEGES = [
    # ── TIER 1 - ELITE BENGALURU INSTITUTIONS (KEA Quota: ~1.12L - 1.21L) ──
    {
        "name": "RVCE", "full_name": "RV College of Engineering, Bengaluru",
        "location": "Bangalore", "naac": "A++", "type": "Autonomous",
        "total_fee": 1.12, "hostel_fee": 1.2, "hostel": True,
        "infrastructure": 9.5, "accreditation": 9.5, "avg_package": 18.0, "highest_package": 45.0, "placement_pct": 95,
        "companies": ["Google", "Microsoft", "Amazon", "Flipkart"], "url": "https://rvce.edu.in",
        "about": "Consistently ranked #1 under KEA choices with legendary technical culture and placements.",
        "branches": {
            "CSE":  {"history": [315, 680, 310, 419, 949]},
            "ISE":  {"history": [450, 890, 520, 610, 1350]},
            "AIML": {"history": [600, 1100, 850, 1050, 2500]},
            "ECE":  {"history": [980, 1800, 1400, 2100, 2900]}
        }
    },
    {
        "name": "PESU-RR", "full_name": "PES University (RR Campus), Bengaluru",
        "location": "Bangalore", "naac": "A+", "type": "Autonomous",
        "total_fee": 1.21, "hostel_fee": 1.5, "hostel": True,
        "infrastructure": 9.2, "accreditation": 9.2, "avg_package": 17.0, "highest_package": 42.0, "placement_pct": 93,
        "companies": ["Adobe", "Apple", "Cisco", "Oracle"], "url": "https://pes.edu",
        "about": "Renowned for its rigorous academic system and heavily competitive coding environment.",
        "branches": {
            "CSE":  {"history": [820, 1100, 1124, 5241, 6056]},
            "ISE":  {"history": [1200, 1600, 1800, 5900, 6800]},
            "AIML": {"history": [1500, 2100, 2400, 6500, 7200]},
            "ECE":  {"history": [2300, 3400, 4100, 8200, 9100]}
        }
    },
    {
        "name": "BMSCE", "full_name": "BMS College of Engineering, Bengaluru",
        "location": "Bangalore", "naac": "A++", "type": "Autonomous",
        "total_fee": 1.12, "hostel_fee": 1.0, "hostel": True,
        "infrastructure": 9.0, "accreditation": 9.0, "avg_package": 15.0, "highest_package": 38.0, "placement_pct": 92,
        "companies": ["Amazon", "TCS", "Infosys", "Wipro"], "url": "https://bmsce.ac.in",
        "about": "One of India's earliest private engineering ventures with an enormous active alumni presence.",
        "branches": {
            "CSE":  {"history": [910, 2200, 1027, 2950, 3870]},
            "ISE":  {"history": [1400, 3100, 1600, 3800, 4900]},
            "AIML": {"history": [1800, 3900, 2100, 4200, 5800]},
            "ECE":  {"history": [2500, 5200, 3400, 6800, 8100]}
        }
    },
    {
        "name": "MSRIT", "full_name": "M.S. Ramaiah Institute of Technology, Bengaluru",
        "location": "Bangalore", "naac": "A+", "type": "Autonomous",
        "total_fee": 1.12, "hostel_fee": 1.1, "hostel": True,
        "infrastructure": 8.8, "accreditation": 8.8, "avg_package": 14.0, "highest_package": 35.0, "placement_pct": 90,
        "companies": ["Capgemini", "Dell", "IBM", "Accenture"], "url": "https://msrit.edu",
        "about": "Highly sought-after corporate training campus located in central Bengaluru.",
        "branches": {
            "CSE":  {"history": [1100, 1000, 1171, 1626, 2076]},
            "ISE":  {"history": [1600, 1800, 2241, 3105, 3400]},
            "AIML": {"history": [2000, 2500, 2800, 3236, 3963]},
            "ECE":  {"history": [3100, 4200, 3268, 4564, 5200]}
        }
    },
    {
        "name": "BIT", "full_name": "Bangalore Institute of Technology, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "Autonomous",
        "total_fee": 1.12, "hostel_fee": 0.85, "hostel": True,
        "infrastructure": 8.2, "accreditation": 8.2, "avg_package": 11.0, "highest_package": 24.0, "placement_pct": 82,
        "companies": ["Mercedes Benz", "TCS", "Bosch", "Sony"], "url": "https://bit-bangalore.edu.in",
        "about": "Established city campus recognized globally for consistent mass recruitment metrics.",
        "branches": {
            "CSE":  {"history": [4200, 6500, 5500, 7200, 8200]},
            "ISE":  {"history": [5800, 8200, 7100, 9100, 10200]},
            "AIML": {"history": [6500, 9200, 8400, 10500, 11800]},
            "ECE":  {"history": [8500, 12000, 11000, 14000, 15500]}
        }
    },

    # ── TIER 2 - REPUTED BANGALORE AND GOVERNMENT CLUSTERS ─────────────────────────
    {
        "name": "UVCE", "full_name": "University Visvesvaraya College of Engineering, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "Government",
        "total_fee": 0.49, "hostel_fee": 0.3, "hostel": True,
        "infrastructure": 8.0, "accreditation": 8.0, "avg_package": 13.0, "highest_package": 30.0, "placement_pct": 87,
        "companies": ["Dell", "L&T", "TCS", "Cognizant"], "url": "https://uvce.ac.in",
        "about": "Historic government institution providing exceptional return on investment statistics.",
        "branches": {
            "CSE":  {"history": [2400, 2929, 3100, 4723, 5020]},
            "ISE":  {"history": [3600, 4100, 4500, 5800, 6400]},
            "AIML": {"history": [4100, 5200, 5800, 7200, 8100]},
            "ECE":  {"history": [5200, 6800, 7200, 9500, 10500]}
        }
    },
    {
        "name": "DSCE", "full_name": "Dayananda Sagar College of Engineering, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "Autonomous",
        "total_fee": 1.12, "hostel_fee": 0.9, "hostel": True,
        "infrastructure": 8.5, "accreditation": 8.5, "avg_package": 12.0, "highest_package": 28.0, "placement_pct": 85,
        "companies": ["Infosys", "Wipro", "HCL Technologies", "IBM"], "url": "https://dayanandasagar.edu",
        "about": "Sprawling infrastructure setup holding partnerships with multiple foreign technical programs.",
        "branches": {
            "CSE":  {"history": [3100, 3677, 4800, 5430, 6584]},
            "ISE":  {"history": [4500, 5200, 6100, 7400, 8500]},
            "AIML": {"history": [5200, 6100, 7400, 8500, 9600]},
            "ECE":  {"history": [8100, 9800, 11500, 13500, 15000]}
        }
    },
    {
        "name": "BMSIT", "full_name": "BMS Institute of Technology and Management, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "Autonomous",
        "total_fee": 1.12, "hostel_fee": 0.8, "hostel": True,
        "infrastructure": 7.8, "accreditation": 7.8, "avg_package": 9.0, "highest_package": 20.0, "placement_pct": 77,
        "companies": ["Capgemini", "Amazon", "Wipro", "KPIT"], "url": "https://bmsit.ac.in",
        "about": "Fast-progressing northern campus sister track to the legacy BMS system.",
        "branches": {
            "CSE":  {"history": [7200, 9800, 11000, 15000, 18000]},
            "ISE":  {"history": [9100, 12000, 14000, 19000, 22000]},
            "AIML": {"history": [10500, 14000, 16500, 22000, 25000]},
            "ECE":  {"history": [14000, 18500, 21000, 29000, 35000]}
        }
    },
    {
        "name": "NMIT", "full_name": "Nitte Meenakshi Institute of Technology, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "Autonomous",
        "total_fee": 1.12, "hostel_fee": 0.95, "hostel": True,
        "infrastructure": 8.4, "accreditation": 8.1, "avg_package": 10.2, "highest_package": 26.0, "placement_pct": 84,
        "companies": ["Microsoft", "Huawei", "Nutanyx", "TCS"], "url": "https://nmit.ac.in",
        "about": "Acclaimed engineering hub famous for its specific aerospace research funding.",
        "branches": {
            "CSE":  {"history": [8900, 11500, 12000, 13500, 14000]},
            "ISE":  {"history": [11200, 14000, 15500, 17000, 18500]},
            "AIML": {"history": [13000, 16000, 17500, 19000, 21000]},
            "ECE":  {"history": [17000, 21000, 23000, 24500, 26000]}
        }
    },
    {
        "name": "RNSIT", "full_name": "RNS Institute of Technology, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "VTU",
        "total_fee": 1.12, "hostel_fee": 0.8, "hostel": True,
        "infrastructure": 8.0, "accreditation": 8.0, "avg_package": 10.0, "highest_package": 22.0, "placement_pct": 80,
        "companies": ["Infosys", "Cognizant", "Mindtree", "LTI"], "url": "https://rnsit.ac.in",
        "about": "Quiet corporate-centric location with heavy focus on software foundational frameworks.",
        "branches": {
            "CSE":  {"history": [9200, 13000, 12000, 16500, 19000]},
            "ISE":  {"history": [12500, 17000, 16000, 21000, 24000]},
            "AIML": {"history": [14000, 19000, 18500, 24000, 27000]},
            "ECE":  {"history": [21000, 29000, 28000, 33000, 36000]}
        }
    },

    # ── TIER 3 - REGIONAL POWERHOUSES (MYSORE, MANGALORE, HUBLI, TUMKUR) ───────────
    {
        "name": "NIE-Mysore", "full_name": "National Institute of Engineering, Mysuru",
        "location": "Mysore", "naac": "A", "type": "Autonomous",
        "total_fee": 1.12, "hostel_fee": 0.8, "hostel": True,
        "infrastructure": 8.3, "accreditation": 8.3, "avg_package": 11.0, "highest_package": 25.0, "placement_pct": 83,
        "companies": ["Cisco", "ABB", "Schneider Electric", "Infosys"], "url": "https://nie.ac.in",
        "about": "One of Karnataka's oldest legacy institutions renowned for deep engineering industry alignment.",
        "branches": {
            "CSE":  {"history": [2100, 3500, 3800, 4200, 4900]},
            "ISE":  {"history": [3400, 4800, 5200, 6100, 6900]},
            "AIML": {"history": [4500, 5900, 6500, 7800, 8600]},
            "ECE":  {"history": [6200, 9200, 11000, 13500, 15000]}
        }
    },
    {
        "name": "JSSSTU", "full_name": "JSS Science & Technology University (SJCE), Mysuru",
        "location": "Mysore", "naac": "A+", "type": "Autonomous",
        "total_fee": 1.12, "hostel_fee": 0.9, "hostel": True,
        "infrastructure": 8.6, "accreditation": 8.6, "avg_package": 12.0, "highest_package": 28.0, "placement_pct": 86,
        "companies": ["Bosch", "Texas Instruments", "Volvo", "Wipro"], "url": "https://jssstuniv.in",
        "about": "Sprawling university grounds producing consistent placement percentages in core disciplines.",
        "branches": {
            "CSE":  {"history": [1500, 2800, 2000, 3156, 3533]},
            "ISE":  {"history": [2400, 3900, 3063, 4500, 4794]},
            "AIML": {"history": [3100, 4600, 3963, 5200, 5800]},
            "ECE":  {"history": [4800, 7200, 6500, 8900, 9600]}
        }
    },
    {
        "name": "KLE-HUBLI", "full_name": "KLE Technological University (BVB), Hubballi",
        "location": "Hubli", "naac": "A+", "type": "Autonomous",
        "total_fee": 1.12, "hostel_fee": 0.8, "hostel": True,
        "infrastructure": 8.2, "accreditation": 8.2, "avg_package": 11.0, "highest_package": 24.0, "placement_pct": 82,
        "companies": ["Samsung", "Amazon", "Deloitte", "TCS"], "url": "https://kletech.ac.in",
        "about": "The ultimate destination for northern region technological advancements and enterprise incubation.",
        "branches": {
            "CSE":  {"history": [4500, 6200, 7500, 9200, 11000]},
            "ISE":  {"history": [6800, 8500, 9800, 12000, 14000]},
            "AIML": {"history": [7500, 9900, 12000, 14500, 17500]},
            "ECE":  {"history": [11000, 15000, 19000, 22000, 24031]}
        }
    },
    {
        "name": "SIT-TUMKUR", "full_name": "Siddaganga Institute of Technology, Tumakuru",
        "location": "Tumkur", "naac": "A", "type": "Autonomous",
        "total_fee": 1.12, "hostel_fee": 0.7, "hostel": True,
        "infrastructure": 7.8, "accreditation": 7.8, "avg_package": 9.0, "highest_package": 20.0, "placement_pct": 78,
        "companies": ["Mphasis", "TCS", "Infosys", "Capgemini"], "url": "https://sit.ac.in",
        "about": "Value-centric education hub known for highly disciplined student development tracks.",
        "branches": {
            "CSE":  {"history": [6500, 9400, 11000, 13200, 14000]},
            "ISE":  {"history": [8900, 12000, 14500, 17000, 19000]},
            "AIML": {"history": [9800, 14000, 16000, 18500, 19500]},
            "ECE":  {"history": [13000, 16500, 17985, 22000, 25000]}
        }
    },
    {
        "name": "CMRIT", "full_name": "CMR Institute of Technology, Bengaluru",
        "location": "Bangalore", "naac": "A+", "type": "VTU",
        "total_fee": 1.12, "hostel_fee": 0.85, "hostel": True,
        "infrastructure": 7.5, "accreditation": 7.5, "avg_package": 8.0, "highest_package": 18.0, "placement_pct": 75,
        "companies": ["Wipro", "HCL", "Mphasis", "Capgemini"], "url": "https://cmrit.ac.in",
        "about": "Strategically placed in the IT corridor, offering robust corporate network exposure.",
        "branches": {
            "CSE":  {"history": [9500, 12000, 11000, 12500, 14000]},
            "ISE":  {"history": [13000, 16000, 14500, 17000, 18500]},
            "AIML": {"history": [15000, 18000, 16000, 19500, 21000]},
            "ECE":  {"history": [22000, 28000, 26000, 31000, 35000]}
        }
    },

    # ── 🌟 PROMINENT HIGHLIGHT: NAGARJUNA COLLEGE OF ENGINEERING AND TECHNOLOGY ──
    {
        "name": "NCET", "full_name": "Nagarjuna College of Engineering and Technology, Bengaluru",
        "location": "Bangalore", "naac": "A+", "type": "Autonomous",
        "total_fee": 1.12, "hostel_fee": 0.85, "hostel": True,
        "infrastructure": 8.4, "accreditation": 8.0, "avg_package": 6.5, "highest_package": 16.0, "placement_pct": 76,
        "companies": ["TCS", "Cognizant", "DXC Technology", "Infosys", "Mindtree"], "url": "https://ncet.co.in",
        "about": "Sprawling state-of-the-art 72-acre campus near Devanahalli with advanced technical labs and incubation infrastructure.",
        "branches": {
            "CSE":  {"history": [45000, 55000, 64000, 68000, 70242]},
            "ISE":  {"history": [52000, 62000, 71000, 74000, 78500]},
            "AIML": {"history": [55000, 66000, 73073, 85000, 93704]},
            "ECE":  {"history": [75000, 88000, 96000, 100736, 117795]}
        }
    },

    # ── COMPREHENSIVE KEA CLUSTER STAPLES (Under the 1.22L Annual Threshold) ──
    {
        "name": "BNMIT", "full_name": "BNM Institute of Technology, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "VTU",
        "total_fee": 1.12, "hostel_fee": 0.9, "hostel": True,
        "infrastructure": 7.6, "accreditation": 7.8, "avg_package": 8.2, "highest_package": 20.0, "placement_pct": 79,
        "companies": ["TCS", "Toyota", "Wipro"], "url": "https://bnmit.org",
        "about": "Acclaimed institution located in South Bangalore known for strict academics and high core standards.",
        "branches": {
            "CSE":  {"history": [6500, 8900, 10000, 11500, 12000]},
            "ISE":  {"history": [8200, 11000, 12500, 14000, 15500]},
            "AIML": {"history": [9500, 13000, 14500, 16000, 17200]},
            "ECE":  {"history": [12000, 16000, 18402, 22000, 24500]}
        }
    },
    {
        "name": "REVA", "full_name": "REVA University, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "Autonomous",
        "total_fee": 1.21, "hostel_fee": 1.2, "hostel": True,
        "infrastructure": 8.9, "accreditation": 8.0, "avg_package": 7.8, "highest_package": 23.0, "placement_pct": 74,
        "companies": ["Deloitte", "IBM", "Capgemini"], "url": "https://reva.edu.in",
        "about": "Massive state-of-the-art green campus in North Bangalore with multi-disciplinary research wings.",
        "branches": {
            "CSE":  {"history": [15000, 19000, 24012, 25000, 26000]},
            "ISE":  {"history": [19000, 24000, 28000, 31000, 33000]},
            "AIML": {"history": [22000, 27000, 29000, 34000, 37000]},
            "ECE":  {"history": [28000, 36000, 38950, 44000, 48000]}
        }
    },
    {
        "name": "MVJCE", "full_name": "MVJ College of Engineering, Bengaluru",
        "location": "Bangalore", "naac": "B++", "type": "VTU",
        "total_fee": 1.12, "hostel_fee": 0.8, "hostel": True,
        "infrastructure": 7.2, "accreditation": 7.0, "avg_package": 6.8, "highest_package": 15.0, "placement_pct": 72,
        "companies": ["Wipro", "HCL", "TCS"], "url": "https://mvjce.edu.in",
        "about": "One of the older engineering choices in East Bangalore with heavy academic training frameworks.",
        "branches": {
            "CSE":  {"history": [22000, 28000, 32000, 36000, 39000]},
            "ISE":  {"history": [28000, 34000, 39000, 44000, 47000]},
            "AIML": {"history": [31000, 39000, 44000, 49000, 53000]},
            "ECE":  {"history": [38000, 48000, 51034, 58000, 64000]}
        }
    },
    {
        "name": "JSSATE", "full_name": "JSS Academy of Technical Education, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "VTU",
        "total_fee": 1.12, "hostel_fee": 0.85, "hostel": True,
        "infrastructure": 7.6, "accreditation": 7.6, "avg_package": 7.2, "highest_package": 16.0, "placement_pct": 73,
        "companies": ["TCS", "Accenture", "Cognizant"], "url": "https://jssateb.ac.in",
        "about": "Backed by the extensive JSS Mahavidyapeetha foundation, ensuring clean placement tracks.",
        "branches": {
            "CSE":  {"history": [12000, 16000, 21000, 24000, 26000]},
            "ISE":  {"history": [16000, 22000, 27000, 31000, 34000]},
            "AIML": {"history": [18000, 25000, 31000, 35000, 39000]},
            "ECE":  {"history": [24000, 32000, 39000, 45000, 50000]}
        }
    },
    {
        "name": "NHCE", "full_name": "New Horizon College of Engineering, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "Autonomous",
        "total_fee": 1.12, "hostel_fee": 1.1, "hostel": True,
        "infrastructure": 8.7, "accreditation": 8.0, "avg_package": 8.5, "highest_package": 24.0, "placement_pct": 81,
        "companies": ["Capgemini", "IBM", "Wipro"], "url": "https://newhorizonindia.edu",
        "about": "Located along the outer ring road IT cluster, enabling premium industry exposures.",
        "branches": {
            "CSE":  {"history": [8500, 11000, 15000, 16500, 18000]},
            "ISE":  {"history": [11000, 14500, 18500, 21000, 23000]},
            "AIML": {"history": [13000, 17000, 21000, 24000, 26000]},
            "ECE":  {"history": [18000, 24000, 31000, 34500, 37027]}
        }
    },
    {
        "name": "AIT", "full_name": "Acharya Institute of Technology, Bengaluru",
        "location": "Bangalore", "naac": "B++", "type": "VTU",
        "total_fee": 1.12, "hostel_fee": 0.8, "hostel": True,
        "infrastructure": 8.5, "accreditation": 7.2, "avg_package": 7.0, "highest_package": 18.0, "placement_pct": 71,
        "companies": ["TCS", "Infosys", "Mphasis"], "url": "https://acharya.ac.in",
        "about": "Vast international campus holding distinct global academic alliance opportunities.",
        "branches": {
            "CSE":  {"history": [14000, 19000, 23000, 27000, 31000]},
            "ISE":  {"history": [19000, 25000, 30000, 35000, 39000]},
            "AIML": {"history": [22000, 29000, 35000, 41000, 46000]},
            "ECE":  {"history": [31000, 42000, 51000, 58000, 64000]}
        }
    },
    {
        "name": "SJCET", "full_name": "SJC Institute of Technology, Chikkaballapur",
        "location": "Chikkaballapur", "naac": "A", "type": "VTU",
        "total_fee": 1.12, "hostel_fee": 0.65, "hostel": True,
        "infrastructure": 7.4, "accreditation": 7.5, "avg_package": 5.6, "highest_package": 12.0, "placement_pct": 70,
        "companies": ["Wipro", "Cognizant", "TCS"], "url": "https://sjcit.ac.in",
        "about": "Renowned regional option offering extensive rural scholarship options and budget pricing metrics.",
        "branches": {
            "CSE":  {"history": [28000, 36000, 48000, 52000, 56000]},
            "ISE":  {"history": [36000, 46000, 58000, 64000, 69000]},
            "AIML": {"history": [41000, 52000, 64000, 71000, 77000]},
            "ECE":  {"history": [52000, 68000, 81000, 89000, 96000]}
        }
    },
    {
        "name": "SMVIT", "full_name": "Sir M. Visvesvaraya Institute of Technology, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "VTU",
        "total_fee": 1.12, "hostel_fee": 0.9, "hostel": True,
        "infrastructure": 7.8, "accreditation": 7.8, "avg_package": 8.0, "highest_package": 22.0, "placement_pct": 78,
        "companies": ["TCS", "Cognizant", "Dell"], "url": "https://sirmvit.edu",
        "about": "Legacy campus near the international airport holding solid reputation with core software recruiters.",
        "branches": {
            "CSE":  {"history": [6200, 8500, 11000, 13000, 14500]},
            "ISE":  {"history": [8500, 11200, 14000, 16500, 18500]},
            "AIML": {"history": [9800, 13000, 16000, 19000, 21000]},
            "ECE":  {"history": [14000, 19000, 23000, 27000, 31000]}
        }
    },
    {
        "name": "SDMCET", "full_name": "SDM College of Engineering and Technology, Dharwad",
        "location": "Dharwad", "naac": "A", "type": "VTU",
        "total_fee": 1.12, "hostel_fee": 0.7, "hostel": True,
        "infrastructure": 7.6, "accreditation": 7.9, "avg_package": 7.5, "highest_package": 16.0, "placement_pct": 74,
        "companies": ["Sony", "TCS", "Infosys"], "url": "https://sdmcet.ac.in",
        "about": "Premier technical college operating across North Karnataka regions with robust lab ecosystems.",
        "branches": {
            "CSE":  {"history": [9500, 14000, 18000, 21000, 24000]},
            "ISE":  {"history": [13000, 19000, 24000, 28000, 31000]},
            "AIML": {"history": [15000, 22000, 27000, 31000, 35000]},
            "ECE":  {"history": [21000, 31000, 39000, 44000, 49000]}
        }
    },
    {
        "name": "PESCE", "full_name": "PES College of Engineering, Mandya",
        "location": "Mandya", "naac": "A", "type": "Autonomous",
        "total_fee": 0.44, "hostel_fee": 0.65, "hostel": True,
        "infrastructure": 7.5, "accreditation": 7.8, "avg_package": 7.0, "highest_package": 15.0, "placement_pct": 75,
        "companies": ["TCS", "Wipro", "Tech Mahindra"], "url": "https://pescemandya.org",
        "about": "Highly respected government-aided institute known for solid research grants and low cost metrics.",
        "branches": {
            "CSE":  {"history": [11000, 16000, 20944, 23000, 25000]},
            "ISE":  {"history": [15000, 21000, 27000, 31000, 34000]},
            "AIML": {"history": [17000, 24000, 31000, 36000, 40000]},
            "ECE":  {"history": [22000, 31000, 39000, 45000, 51000]}
        }
    },
    {
        "name": "DSATM", "full_name": "Dayananda Sagar Academy of Technology and Management, Bengaluru",
        "location": "Bangalore", "naac": "A+", "type": "VTU",
        "total_fee": 1.12, "hostel_fee": 0.9, "hostel": True,
        "infrastructure": 8.2, "accreditation": 7.8, "avg_package": 7.5, "highest_package": 18.0, "placement_pct": 76,
        "companies": ["Infosys", "IBM", "Cognizant"], "url": "https://dsatm.edu.in",
        "about": "Modern global campus unit running shared recruitment channels with the main DSCE infrastructure track.",
        "branches": {
            "CSE":  {"history": [9500, 13000, 17000, 19500, 22000]},
            "ISE":  {"history": [13000, 17500, 22000, 25000, 28000]},
            "AIML": {"history": [15000, 19500, 25000, 29000, 32000]},
            "ECE":  {"history": [21000, 29000, 37027, 42000, 47000]}
        }
    },
    {
        "name": "MSRUAS", "full_name": "M.S. Ramaiah University of Applied Sciences, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "Autonomous",
        "total_fee": 1.21, "hostel_fee": 1.1, "hostel": True,
        "infrastructure": 8.4, "accreditation": 7.6, "avg_package": 7.6, "highest_package": 19.0, "placement_pct": 75,
        "companies": ["Amazon", "TCS", "Wipro"], "url": "https://msruas.ac.in",
        "about": "Ramaiah's core university cluster focusing on advanced engineering application skillsets.",
        "branches": {
            "CSE":  {"history": [7500, 9800, 12913, 15000, 17000]},
            "ISE":  {"history": [9800, 13000, 17000, 21000, 24000]},
            "AIML": {"history": [11000, 15500, 19500, 24000, 27000]},
            "ECE":  {"history": [16000, 23000, 31000, 37000, 42000]}
        }
    },
    {
        "name": "PRESIDENCY", "full_name": "Presidency University, Bengaluru",
        "location": "Bangalore", "naac": "A+", "type": "Autonomous",
        "total_fee": 1.21, "hostel_fee": 1.3, "hostel": True,
        "infrastructure": 9.1, "accreditation": 8.0, "avg_package": 7.2, "highest_package": 16.0, "placement_pct": 73,
        "companies": ["Capgemini", "Wipro", "TCS"], "url": "https://presidencyuniversity.in",
        "about": "Ultra-modern premium infrastructure setups holding multi-stage incubation programs.",
        "branches": {
            "CSE":  {"history": [18000, 26000, 35000, 38000, 42000]},
            "ISE":  {"history": [24000, 34000, 44000, 49000, 54000]},
            "AIML": {"history": [27000, 38000, 48000, 54000, 61000]},
            "ECE":  {"history": [36000, 49000, 62000, 69000, 78000]}
        }
    },
    {
        "name": "DSU", "full_name": "Dayananda Sagar University, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "Autonomous",
        "total_fee": 1.21, "hostel_fee": 1.3, "hostel": True,
        "infrastructure": 8.6, "accreditation": 8.0, "avg_package": 8.0, "highest_package": 21.0, "placement_pct": 77,
        "companies": ["Cognizant", "TCS", "Infosys"], "url": "https://dsu.edu.in",
        "about": "Hi-tech research university with specific corporate-sponsored labs built right inside the campus.",
        "branches": {
            "CSE":  {"history": [11000, 16000, 25303, 28000, 31000]},
            "ISE":  {"history": [15000, 21000, 31000, 35000, 39000]},
            "AIML": {"history": [17000, 24000, 35000, 40000, 45000]},
            "ECE":  {"history": [24000, 34000, 46000, 52000, 58000]}
        }
    },
    {
        "name": "RVU", "full_name": "RV University, Bengaluru",
        "location": "Bangalore", "naac": "A", "type": "Autonomous",
        "total_fee": 1.21, "hostel_fee": 1.4, "hostel": True,
        "infrastructure": 9.2, "accreditation": 8.5, "avg_package": 10.5, "highest_package": 28.0, "placement_pct": 82,
        "companies": ["Deloitte", "Microsoft", "Google"], "url": "https://rvu.edu.in",
        "about": "The premium university branch of the iconic RV family focusing on state-of-the-art computational algorithms.",
        "branches": {
            "CSE":  {"history": [3500, 5200, 7162, 8100, 9200]},
            "ISE":  {"history": [4800, 6800, 9500, 11000, 12500]},
            "AIML": {"history": [5500, 7800, 11000, 13000, 14800]},
            "ECE":  {"history": [8200, 11000, 16000, 19000, 21500]}
        }
    }
]
