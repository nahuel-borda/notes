# Notes

Truquen is a Discord bot that allows users to play the popular Argentinian card game, Truco. With Truquen, you can create private games with your friends and enjoy playing Truco in the comfort of your own Discord server.

## Installation

To install Notes, please follow the instructions below:

1. Clone the repository using the following command:
```
git clone https://github.com/nahuel-borda/truquen.git
```
2. Navigate to the cloned directory using the following command:
```
cd truquen
```
3. Install the required packages using the following command:
```
pip install -r requirements.txt
```
4. Create the database using the following command:
```
python manage.py migrate
```
5. Create a superuser account using the following command and follow the prompts:
```
python manage.py createsuperuser
```
6. Start the server using the following command:
```
python manage.py runserver
```
That's it! You should now have Notes up and running on your local machine.


## Usage

To use Notes, follow these steps:

1. Open your web browser and navigate to http://localhost:8000/.
2. Log in to the administration panel using your superuser account.
3. Create a new note by clicking the "Add note" button and filling out the form.
4. View and edit your notes by navigating to the "Notes" section of the administration panel.
5. Search for a note by using the search bar at the top of the page.

## Contributing

If you'd like to contribute to Notes, please follow the instructions below:

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your changes.
3. Make your changes and test them locally.
4. Commit your changes with a clear and concise commit message.
5. Push your changes to your forked repository.
6. Create a pull request and describe your changes.
