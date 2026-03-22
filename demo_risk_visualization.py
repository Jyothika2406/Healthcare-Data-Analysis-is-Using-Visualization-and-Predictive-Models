"""
Demo: Risk Visualization Feature
This script demonstrates the new risk visualization functionality.
"""

def demo_risk_analysis():
    """Demonstrate how the risk analysis works with sample data"""
    
    print("🏥 HEALTHCARE RISK VISUALIZATION DEMO")
    print("=" * 50)
    
    # Sample user input (similar to what comes from the health form)
    sample_user_data = {
        'age': 52,
        'gender': 'Male', 
        'blood_pressure': 145,
        'sugar_level': 130,
        'height': 175,
        'weight': 85,
        'bmi': 27.8,
        'symptoms': 'chest pain, occasional shortness of breath',
        'smoking': True,
        'exercise': False,
        'alcohol': True
    }
    
    print("📝 SAMPLE USER INPUT:")
    print(f"   Age: {sample_user_data['age']} years")
    print(f"   Gender: {sample_user_data['gender']}")
    print(f"   Blood Pressure: {sample_user_data['blood_pressure']} mmHg")
    print(f"   Blood Sugar: {sample_user_data['sugar_level']} mg/dl")
    print(f"   Height: {sample_user_data['height']} cm")
    print(f"   Weight: {sample_user_data['weight']} kg")
    print(f"   BMI: {sample_user_data['bmi']}")
    print(f"   Symptoms: {sample_user_data['symptoms']}")
    print(f"   Smoking: {'Yes' if sample_user_data['smoking'] else 'No'}")
    print(f"   Regular Exercise: {'Yes' if sample_user_data['exercise'] else 'No'}")
    print(f"   Alcohol: {'Yes' if sample_user_data['alcohol'] else 'No'}")
    
    print("\n🔍 RISK FACTOR ANALYSIS:")
    
    # Simulate risk factor analysis
    risk_factors = []
    
    # Age analysis
    age = sample_user_data['age']
    if age > 50:
        risk_factors.append({
            'factor': 'Age',
            'value': f'{age} years',
            'risk_level': 'Medium',
            'impact': 15,
            'explanation': 'Age over 50 increases cardiovascular risk'
        })
    
    # Blood pressure analysis  
    bp = sample_user_data['blood_pressure']
    if bp > 140:
        risk_factors.append({
            'factor': 'Blood Pressure', 
            'value': f'{bp} mmHg',
            'risk_level': 'High',
            'impact': 25,
            'explanation': 'Blood pressure >140 indicates hypertension'
        })
    
    # Blood sugar analysis
    sugar = sample_user_data['sugar_level'] 
    if sugar > 126:
        risk_factors.append({
            'factor': 'Blood Sugar',
            'value': f'{sugar} mg/dl', 
            'risk_level': 'Medium',
            'impact': 15,
            'explanation': 'Elevated fasting glucose indicates diabetes risk'
        })
    
    # BMI analysis
    bmi = sample_user_data['bmi']
    if bmi > 25:
        risk_factors.append({
            'factor': 'BMI',
            'value': f'{bmi:.1f}',
            'risk_level': 'Medium',
            'impact': 12,
            'explanation': 'BMI >25 indicates overweight'
        })
    
    # Smoking analysis
    if sample_user_data['smoking']:
        risk_factors.append({
            'factor': 'Smoking',
            'value': 'Yes',
            'risk_level': 'High', 
            'impact': 25,
            'explanation': 'Smoking significantly increases cardiovascular risk'
        })
    
    # Exercise analysis
    if not sample_user_data['exercise']:
        risk_factors.append({
            'factor': 'Physical Activity',
            'value': 'Sedentary',
            'risk_level': 'Medium',
            'impact': 18,
            'explanation': 'Lack of exercise increases health risks'
        })
    
    # Display risk factors
    for i, factor in enumerate(risk_factors, 1):
        risk_emoji = '🔴' if factor['risk_level'] == 'High' else '🟡' if factor['risk_level'] == 'Medium' else '🟢'
        print(f"   {i}. {risk_emoji} {factor['factor']}: {factor['value']}")
        print(f"      Risk Level: {factor['risk_level']} (Impact: {factor['impact']}%)")
        print(f"      {factor['explanation']}")
        print()
    
    # Calculate overall risk
    total_risk_score = sum(factor['impact'] for factor in risk_factors)
    
    print("📊 OVERALL ASSESSMENT:")
    print(f"   Total Risk Score: {total_risk_score}%")
    
    if total_risk_score >= 80:
        overall_risk = "High Risk"
        risk_emoji = "⚠️"
        recommendation = "Immediate medical consultation recommended"
    elif total_risk_score >= 50:
        overall_risk = "Medium Risk"
        risk_emoji = "⚡"
        recommendation = "Regular monitoring and lifestyle changes advised"
    else:
        overall_risk = "Low Risk" 
        risk_emoji = "✅"
        recommendation = "Maintain healthy lifestyle habits"
    
    print(f"   {risk_emoji} Risk Level: {overall_risk}")
    print(f"   Recommendation: {recommendation}")
    
    print("\n🎯 VISUALIZATION FEATURES:")
    print("   📊 Risk Factor Breakdown Chart (Doughnut)")
    print("   📈 Individual Factor Impact Chart (Bar)")
    print("   📋 Interactive Risk Factors Summary")
    print("   🎨 Color-coded Risk Indicators")
    print("   📱 Responsive Design for All Devices")
    
    print("\n🔄 USER EXPERIENCE FLOW:")
    print("   1. User fills health form")
    print("   2. AI analyzes health data") 
    print("   3. Automatic redirect to dashboard")
    print("   4. Risk visualization appears prominently")
    print("   5. User can explore factors and take action")
    
    return True

if __name__ == "__main__":
    demo_risk_analysis()
    
    print("\n" + "=" * 50)
    print("🚀 The risk visualization feature is now ready!")
    print("📝 Test it by running the Flask app and submitting a health form.")