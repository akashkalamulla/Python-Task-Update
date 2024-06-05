from app import 

app = create_app('config/config.py')

if __name__ == '__main__':
    app.run(debug=True)

  