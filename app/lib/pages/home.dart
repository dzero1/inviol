import 'package:app/components/eventForm.dart';
import 'package:app/components/eventItem.dart';
import 'package:app/models/event.dart';
import 'package:app/services/http.dart';
import 'package:dio/dio.dart';
import 'package:flutter/material.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  List events = [];

  void getEvents() async {
    try {
      final response = await dio.get('/events');
      events = response.data.map((e) => Event.fromJson(e)).toList();
      setState(() {});
    } on DioException catch (e) {
      ScaffoldMessenger.of(context).clearSnackBars();
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(e.response?.data ?? e.message),
          backgroundColor: Colors.green,
        ),
      );
    }
  }

  @override
  void initState() {
    super.initState();
    getEvents();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: ListView.builder(
        itemCount: events.length,
        itemBuilder: (context, index) =>
            EventItemView(eventData: events[index]),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          // open event create form as dialog
          showDialog(
            context: context,
            builder: (context) => const EventCreateForm(),
            barrierDismissible: false,
            useRootNavigator: false,
          ).then((value) => getEvents());
        },
        tooltip: 'Create Event',
        child: const Icon(Icons.add),
      ),
    );
  }
}
