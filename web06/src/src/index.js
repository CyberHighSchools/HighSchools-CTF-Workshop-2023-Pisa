const express = require('express');
const app = express();
const bodyParser = require('body-parser'); // Add this line

const FLAG = process.env.FLAG || 'flag{test_flag}';

// Sample data object
const data = {
    flag: FLAG,
};

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true })); // Add this line

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html'); // Serve the HTML file
});

// Handle the POST request
app.get('/element', (req, res) => {
    const element = req.query.element;
    var content =  '';
    if (element === 'flag'){
        content = 'you wish'
    }else{
        content = data[element] || 'Element not found';
    }
    
    // Send HTML response with dynamic content
    res.send(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Element Content</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="text-center">Element Content</h1>
            <div class="card mt-4">
                <div class="card-body">
                    <p class="mb-0"><strong>Element:</strong> ${element}</p>
                    <p class="mb-0"><strong>Content:</strong> ${content}</p>
                </div>
            </div>
            <a href="/" class="btn btn-primary mt-4">Back</a>
        </div>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>    
    `);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
