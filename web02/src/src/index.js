const express = require('express');
const cookieParser = require("cookie-parser");

const app = express();
app.engine('html', require('ejs').renderFile);
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(cookieParser());


let db = {};

const set_session = (res, data) => {
  data = {
    user:data
  };
  let session_cookie = JSON.stringify(data);
  res.cookie('session', session_cookie, { maxAge: 900000, httpOnly: true });
}

const register = (username, password) => {
  if (!username && !password && typeof username !== "string" || typeof password !== "string")
    return {
      "error": "Missing data"
    };

  if (username.length < 8 || password.length < 8)
    return {
      "error": "Username or password too short"
    };

  if (db[username])
    return {
      "error": "Duplicate user"
    };

  db[username] = {
    username,
    password,
    is_admin: false,
    description: null,
    notes: []
  };

  return db[username];
}

app.get('/login', (req, res) => {
  return res.render('login.html');
});

app.post('/api/login', (req, res) => {
  const { username, password } = req.body;

  if (username && typeof username == "string" && db[username] && db[username].password === password) {
    set_session(res, db[username]);
    return res.status(201).send({
      "ok":"ok"
    });
  }

  return res.send({
    "error": "Invalid credentials"
  });
})

app.get('/register', (req, res) => {
  return res.render('register.html');
});

app.post('/api/register', (req, res) => {
  const data = register(req.body.username, req.body.password);

  if (data.error){
    return res.status(400).send(data);  
  }

  return res.status(201).send(data);
})

/* IsAuth middleware */
app.use((req, res, next) => {
  if (!req.cookies.session)
    return res.redirect('/login');

  try{
    let session = req.cookies.session;
    session = JSON.parse(session);

    if (!session.user || !session.user.username || typeof session.user.username !== "string" || !db.hasOwnProperty(session.user.username))
      return res.redirect('/login');

    req.session = session;
  }
  catch (e){
    return res.redirect('/login');
  }

  return next();
});

app.get('/', (req, res) => {
  return res.render('home.html', { user: db[req.session.user.username] });
});

app.post('/api/edit_description', (req, res) => {
  const { description } = req.body;

  if (description && typeof description === 'string' && description.length < 100){
    db[req.session.user.username].description = description;
    set_session(res, db[req.session.user.username]);
    return res.status(201).send({
      "ok":"ok"
    });
  }

  return res.status(400).send({
    "error" : "Invalid data"
  });
});

app.post('/api/add_note', (req, res) => {
  const { note } = req.body;

  if (note && typeof note === 'string' && note.length < 100){
    db[req.session.user.username].notes.push(note);
    set_session(res, db[req.session.user.username]);
    return res.status(201).send({
      "ok":"ok"
    });
  }

  return res.status(400).send({
    "error" : "Invalid data"
  });
});

app.get('/admin', (req, res) => {
  return res.send(req.session.user.is_admin === true ? (process.env.FLAG || 'FLAG{flag}') : 'Not an admin :P');
})

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
