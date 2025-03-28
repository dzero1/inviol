import 'package:dio/dio.dart';

final options = BaseOptions(
  baseUrl: 'http://localhost:8000',
  connectTimeout: Duration(seconds: 10),
  receiveTimeout: Duration(seconds: 30),
  headers: {
    'content-type': 'application/json',
  },
);

final dio = Dio(options);
