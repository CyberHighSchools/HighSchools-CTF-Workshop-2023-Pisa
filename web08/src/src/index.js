const express = require('express');
const cookieParser = require("cookie-parser");
const sessions = require('express-session');

const app = express();
app.use(sessions({
  secret: process.env.SECRET || 'secret',
  saveUninitialized: true,
  cookie: { maxAge: 1000 * 60 * 60 * 24 },
  resave: false
}));
app.engine('html', require('ejs').renderFile);
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(cookieParser());


let db = {};

const register = (data) => {
  const { username, password, is_admin } = data;

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
    is_admin,
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
    req.session.user = db[username];
    return res.status(201).send({
      "ok": "ok"
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
  const data = register({
    is_admin: false,
    ...req.body
  });

  if (data.error) {
    return res.status(400).send(data);
  }

  return res.status(201).send(data);
})

/* IsAuth middleware */
app.use((req, res, next) => {
  if (!req.session.user || !db[req.session.user.username])
    return res.redirect('/login');

  return next();
});

app.get('/', (req, res) => {
  return res.render('home.html', { user: req.session.user });
});

app.post('/api/edit_description', (req, res) => {
  const { description } = req.body;

  if (description && typeof description === 'string' && description.length < 100) {
    db[req.session.user.username].description = description;
    req.session.user = db[req.session.user.username];
    return res.status(201).send({
      "ok": "ok"
    });
  }

  return res.status(400).send({
    "error": "Invalid data"
  });
});

app.post('/api/add_note', (req, res) => {
  const { note } = req.body;

  if (note && typeof note === 'string' && note.length < 100) {
    db[req.session.user.username].notes.push(note);
    req.session.user = db[req.session.user.username];
    return res.status(201).send({
      "ok": "ok"
    });
  }

  return res.status(400).send({
    "error": "Invalid data"
  });
});

app.get('/admin', (req, res) => {
  return res.send(req.session.user.is_admin === true ? (process.env.FLAG || 'FLAG{flag}') : 'Not an admin :P');
})

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
