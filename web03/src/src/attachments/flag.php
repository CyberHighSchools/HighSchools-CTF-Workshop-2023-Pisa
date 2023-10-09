<?php

if (isset($_POST['password'])) {
    if ($_POST['password'] !== $_ENV['PASSWORD']) {
        header('Location: roll.html');
    }
?>

    <!DOCTYPE html>
    <html>
        <?php echo $_ENV["FLAG"]; ?>
    </html>

<?php } ?>
