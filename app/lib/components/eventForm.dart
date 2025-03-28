import 'dart:convert';

import 'package:app/models/event.dart';
import 'package:flutter/material.dart';
import 'package:flutter_datetime_picker_plus/flutter_datetime_picker_plus.dart'
    as picker;

class EventCreateForm extends StatefulWidget {
  const EventCreateForm({super.key});

  @override
  State<EventCreateForm> createState() => _EventCreateFormState();
}

class _EventCreateFormState extends State<EventCreateForm> {
  final _formKey = GlobalKey<FormState>();

  String? _devideId;
  String? _description;
  String? _meta;
  // DateTime? _timestamp;

  TextEditingController _timestampController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Dialog(
      child: SingleChildScrollView(
        child: Container(
          width: MediaQuery.of(context).size.width < 600
              ? double.infinity
              : MediaQuery.of(context).size.width * 0.6,
          padding: const EdgeInsets.all(12.0),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                //  dialog title
                const Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Center(
                      child: Text(
                        "Add Event",
                        style: TextStyle(
                            fontSize: 22, fontWeight: FontWeight.w600),
                      ),
                    ),
                    Align(
                      alignment: Alignment.topRight,
                      child: CloseButton(),
                    ),
                  ],
                ),
                const SizedBox(height: 16),

                // device id
                FormField(
                  title: "Device ID",
                  onChanged: (value) {
                    _devideId = value;
                  },
                ),

                // Description
                FormField(
                  title: "Description",
                  onChanged: (value) {
                    _description = value;
                  },
                ),

                // Description
                FormField(
                  title: "Timestamp",
                  controller: _timestampController,
                  onTap: () async {
                    debugPrint("onTap");
                    picker.DatePicker.showDateTimePicker(context,
                        showTitleActions: true, onChanged: (date) {
                      print('change  $date');
                    }, onConfirm: (date) {
                      print('confirm $date');

                      _timestampController =
                          TextEditingController(text: date.toIso8601String());
                      setState(() {});
                    });
                  },
                ),

                // Description
                FormField(
                  title: "Meta data",
                  onChanged: (value) {
                    _meta = value;
                  },
                ),

                Align(
                  alignment: Alignment.bottomRight,
                  child: ElevatedButton(
                    onPressed: () async {
                      if (_formKey.currentState!.validate()) {
                        // If the form is valid, display a snackbar. In the real world,
                        // you'd often call a server or save the information in a database.
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(content: Text('Processing Data')),
                        );

                        try {
                          Event event = Event(
                            device_id: _devideId!,
                            timestamp:
                                DateTime.parse(_timestampController.value.text),
                            description: _description,
                            meta: json.decode(_meta ?? "{}"),
                          );
                          // print(event);
                          bool save = await event.save();
                          if (save) {
                            ScaffoldMessenger.of(context).clearSnackBars();
                            ScaffoldMessenger.of(context).showSnackBar(
                              const SnackBar(
                                content: Text('Event saved successfully'),
                                backgroundColor: Colors.green,
                              ),
                            );
                            Navigator.pop(context, true);
                          } else {
                            ScaffoldMessenger.of(context).clearSnackBars();
                            ScaffoldMessenger.of(context).showSnackBar(
                              const SnackBar(
                                content: Text('Failed to save event'),
                                backgroundColor: Colors.red,
                              ),
                            );
                          }
                        } catch (e) {
                          ScaffoldMessenger.of(context).clearSnackBars();
                          print(e);

                          if (e.toString().contains("not valid JSON")) {
                            ScaffoldMessenger.of(context).showSnackBar(
                              const SnackBar(
                                content:
                                    Text('Invalid JSON for Meta Data field'),
                                backgroundColor: Colors.red,
                              ),
                            );
                          }
                        }
                      }
                    },
                    child: const Text(
                      'Save',
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class FormField extends StatelessWidget {
  const FormField(
      {super.key,
      required this.title,
      this.controller,
      this.onChanged,
      this.onTap});

  final Function(String?)? onChanged;
  final String title;
  final GestureTapCallback? onTap;
  final TextEditingController? controller;

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 15),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            title,
            style: const TextStyle(
              fontSize: 16,
              fontWeight: FontWeight.w600,
            ),
          ),
          TextFormField(
            controller: controller,
            decoration: InputDecoration(
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(6),
              ),
            ),
            onChanged: onChanged,
            onTap: onTap,
            validator: (value) =>
                value!.isEmpty ? 'Please enter a $title' : null,
          ),
        ],
      ),
    );
  }
}
