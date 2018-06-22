import 'package:flutter/material.dart';

void main() => runApp(new MyApp());

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
        leading:  new IconButton(icon: new Icon(Icons.list), onPressed: (){}, )

      ),
      floatingActionButton: new FloatingActionButton(
        tooltip: 'Create new Message',
        child: new Icon(Icons.edit), onPressed: () {},backgroundColor: Colors.red,
      ),
    );
  }
}
