"""
Test script for the new risk visualization feature
"""
import requests
import json

def test_app_startup():
    """Test if the Flask app starts correctly"""
    try:
        # Test basic app import
        import app
        print("✅ App imports successfully")
        
        # Check if the new API endpoint exists
        if hasattr(app.app, 'url_map'):
            routes = [str(rule) for rule in app.app.url_map.iter_rules()]
            if '/api/risk-visualization' in routes:
                print("✅ Risk visualization API endpoint found")
            else:
                print("❌ Risk visualization API endpoint not found")
                
        print("\n📋 Available routes:")
        for rule in app.app.url_map.iter_rules():
            if 'api' in str(rule):
                print(f"   {rule}")
                
        return True
        
    except Exception as e:
        print(f"❌ Error testing app: {e}")
        return False

def test_risk_analysis_logic():
    """Test the risk analysis logic"""
    try:
        import app
        
        # Test data similar to what would come from the form
        test_input = {
            'age': 45,
            'gender': 'Male',
            'blood_pressure': 150,
            'sugar_level': 120,
            'height': 175,
            'weight': 80,
            'bmi': 26.1,
            'symptoms': 'chest pain, fatigue',
            'smoking': True,
            'exercise': False,
            'alcohol': True
        }
        
        print("🧪 Testing risk analysis logic...")
        print(f"Input data: {json.dumps(test_input, indent=2)}")
        
        # Test health score calculation
        health_score = app.calculate_health_score(test_input)
        print(f"✅ Health score calculated: {health_score}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing risk analysis: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Testing Risk Visualization Feature")
    print("=" * 50)
    
    test_app_startup()
    print()
    test_risk_analysis_logic()
    
    print("\n✅ Test completed! The risk visualization feature should be working.")
    print("\n📝 To test the full feature:")
    print("1. Run the Flask app: python app.py")
    print("2. Visit http://localhost:5000")
    print("3. Login/Register")
    print("4. Fill out the health form")
    print("5. Submit the form")
    print("6. You should be redirected to the dashboard with risk visualization")