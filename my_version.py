"""Random quiz generator which generates a quiz of india states capitals."""
import random

# Indian states(36 states, 28 states, 8 union territories)capitals dictionary.
capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata",
    # Union Territories
    "Andaman and Nicobar Islands": "Port Blair",
    "Chandigarh": "Chandigarh",
    "Dadra and Nagar Haveli and Daman and Diu": "Daman",
    "Lakshadweep": "Kavaratti",
    "Delhi": "New Delhi",
    "Puducherry": "Puducherry",
    "Ladakh": "Leh",
    "Jammu and Kashmir": "Srinagar",
}

# I am making 40 quizs so creating 40 quiz files
for quiz_num in range(40):
    quiz_file = open(f'Quiz{quiz_num+1}.txt', 'w', encoding='utf-8')
    answer_file = open(f'Ans{quiz_num+1}.txt', 'w', encoding='utf-8')

    # writing the starting content in my files
    quiz_file.write("\n\nName:\n\nDate:\n\nRoll no.:\n\n")
    quiz_file.write(" " * 20 + f"States Capitals Quiz (Set{quiz_num+1})")
    quiz_file.write("\n\n")
