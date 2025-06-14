* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Open Sans', sans-serif;
}

body {
  background: #1bace5da;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.profile-container {
  text-align: center;
  width: 350px;
}

.avatar img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  border: 5px solid #ffffff;
  margin-bottom: -50px;
  z-index: 2;
  position: relative;
  object-fit: cover;
}

.form-container {
  background-color: #6bb3e4;
  padding: 60px 30px 30px;
  border-radius: 3px;
  position: relative;
  box-shadow: 0 0 10px rgba(0,0,0,0.3);
}

h2 {
  color: #fdffff;
  font-size: 18px;
  margin-bottom: 20px;
}

.input-group {
  margin-bottom: 15px;
}

.input-group input {
  width: 100%;
  padding: 10px;
  border: none;
  background: #ecf4f492;
  color: #333;
  font-size: 14px;
  border-radius: 3px;
}

button {
  width: 100%;
  padding: 10px;
  border: none;
  background-color: #5be6dd;
  color: #fff;
  font-size: 16px;
  border-radius: 3px;
  cursor: pointer;
}

button:hover {
  background-color: #3fc3c3;
}

footer {
  margin-top: 15px;
  font-size: 11px;
  color: #eee;
}
