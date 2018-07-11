import 'package:flutter/material.dart';

void main() => runApp(new MyApp());
const String Name = 'Ayush Srivastava';
const String Email = 'sri.ayush777@gmail.com';
const String abbreviation = 'AS';

class MyApp extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      title: 'Primary',
      theme: new ThemeData(

        primarySwatch: Colors.red,
      ),
      home: new MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
    @override
   createState() => new _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

    @override
  Widget build(BuildContext context) {

    return new Scaffold(
      appBar: new AppBar(
          title :new Text('Primary'),
          actions: <Widget>[
            new IconButton(icon: new Icon(Icons.search), onPressed: (){}, )
          ],

      ),

      floatingActionButton: new FloatingActionButton(
        tooltip: 'Create new Message',
        child: new Icon(Icons.edit), onPressed: () {},backgroundColor: Colors.red,
      ),
      drawer: new Drawer(
        child: new ListView(
          padding: EdgeInsets.zero,
          children: <Widget>[
           new UserAccountsDrawerHeader(
               accountName: const Text(Name),
        accountEmail: const Text(Email),
        currentAccountPicture: new CircleAvatar(
          backgroundColor: Colors.lightGreen,
          child: new Text(abbreviation),
        )

      ),
            new ListTile(

              title: Text('All Inboxes'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new Divider(),
            new ListTile(
              leading: new Icon(Icons.inbox),
              title: Text('Primary'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new ListTile(
              leading: new Icon(Icons.people),
              title: Text('Social'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new Divider(),
            new ListTile(
               title: Text('All labels'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new ListTile(
              leading: new Icon(Icons.star),
              title: Text('Starred'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new ListTile(
              leading: new Icon(Icons.label),
              title: Text('Important'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
           new ListTile(
              leading: new Icon(Icons.send),
              title: Text('Sent'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new ListTile(
              leading: new Icon(Icons.cloud_circle),
              title: Text('Outbox'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new ListTile(
                leading: new Icon(Icons.drafts),
                title: Text('Drafts'),
                onTap: () {
                  Navigator.pop(context);
                },
              ),
            new ListTile(
              leading: new Icon(Icons.crop_square),
              title: Text('All mail'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new ListTile(
              leading: new Icon(Icons.error),
              title: Text('Spam'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
           new ListTile(
              leading: new Icon(Icons.delete),
              title: Text('Bin'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new ListTile(
              leading: new Icon(Icons.label),
              title: Text('Unwanted'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new Divider(),
            new ListTile(

              title: Text('Google apps'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new ListTile(
              leading: new Icon(Icons.calendar_today),
              title: Text('Calender'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new ListTile(
              leading: new Icon(Icons.contacts),
              title: Text('Contacts'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new Divider(),
            new ListTile(
              leading: new Icon(Icons.settings),
              title: Text('Settings'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            new ListTile(
              leading: new Icon(Icons.help),
              title: Text('Help & feedback'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
          ],
        ),
      ),
    );
    }
}