"""
Simple script to start the Flask server
"""
import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 60)
print(" HEALTHCARE DATA ANALYSIS - STARTING SERVER")
print("=" * 60)

try:
    print(" Loading Flask application...")
    from app import app
    
    print(" App loaded successfully!")
    print(" Starting server on http://localhost:5000")
    print("=" * 60)
    print(" To access the application:")
    print("   1. Open your browser")
    print("   2. Go to: http://localhost:5000")
    print("   3. Register/login to start using the app")
    print("=" * 60)
    print(" Press CTRL+C to stop the server")
    print("=" * 60)
    
    # Start the Flask app
    debug_mode = os.environ.get('FLASK_ENV', 'development') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000, use_reloader=False)
    
except ImportError as e:
    print(f" Import Error: {e}")
    print("   Please ensure all dependencies are installed:")
    print("   pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f" Error: {e}")
    sys.exit(1)
