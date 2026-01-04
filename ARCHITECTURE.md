# Apache Signal Architecture for Educational Platform

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Apache Web Server                             │
│  (Handles SIGUSR1, SIGTERM, SIGHUP signals)                     │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     │ mod_wsgi
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                   WSGI Application                               │
│              (educational_platform/wsgi.py)                      │
│  - Registers Apache signal handlers                             │
│  - Graceful restart/shutdown support                            │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Django Application                            │
│              (educational_platform)                              │
│  - Settings with logging configuration                          │
│  - URL routing                                                   │
│  - Middleware stack                                              │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Courses App                                   │
│                (courses.apps.CoursesConfig)                      │
│  - Registers signal handlers on app ready                       │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Django Models                                  │
│                  (courses/models.py)                             │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Course        │ Lesson      │ Enrollment                 │  │
│  │ Assignment    │ Submission                               │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│               Django Signal Handlers                             │
│                (courses/signals.py)                              │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  For Each Model:                                          │  │
│  │  - pre_save    (before database write)                   │  │
│  │  - post_save   (after database write)                    │  │
│  │  - pre_delete  (before database delete)                  │  │
│  │  - post_delete (after database delete)                   │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Logging System                               │
│  - Console output (formatted logs)                              │
│  - File output (apache_signals.log)                             │
│  - Timestamp, module, process/thread info                       │
└─────────────────────────────────────────────────────────────────┘
```

## Signal Flow for Model Operations

### Create Operation (POST)
```
User Request → Django View → Model.objects.create()
    ↓
pre_save signal → Signal Handler → Logger
    ↓
Database INSERT
    ↓
post_save signal → Signal Handler → Logger
    ↓
Response to User
```

### Update Operation (PUT/PATCH)
```
User Request → Django View → instance.save()
    ↓
pre_save signal → Signal Handler → Logger
    ↓
Database UPDATE
    ↓
post_save signal → Signal Handler → Logger
    ↓
Response to User
```

### Delete Operation (DELETE)
```
User Request → Django View → instance.delete()
    ↓
pre_delete signal → Signal Handler → Logger
    ↓
Database DELETE
    ↓
post_delete signal → Signal Handler → Logger
    ↓
Response to User
```

## Apache Signal Types

### SIGUSR1 (Graceful Restart)
- Command: `apachectl graceful`
- Effect: Gracefully restart worker processes
- Handler: `handle_sigusr1()` in wsgi.py

### SIGTERM (Shutdown)
- Command: `apachectl stop`
- Effect: Terminate all processes
- Handler: `handle_sigterm()` in wsgi.py

### SIGHUP (Configuration Reload)
- Command: `apachectl restart`
- Effect: Reload configuration
- Handler: `handle_sighup()` in wsgi.py

## Model Signal Coverage

| Model      | pre_save | post_save | pre_delete | post_delete |
|------------|----------|-----------|------------|-------------|
| Course     | ✓        | ✓         | ✓          | ✓           |
| Lesson     | ✓        | ✓         | ✓          | ✓           |
| Enrollment | ✓        | ✓         | ✓          | ✓           |
| Assignment | ✓        | ✓         | ✓          | ✓           |
| Submission | ✓        | ✓         | ✓          | ✓           |

**Total: 20 signal handlers across 5 models**

## Theia IDE Integration

Theia IDE provides:
- Full terminal access for testing signals
- File editing for signal handlers
- Log file viewing (apache_signals.log)
- Development server execution
- Database shell access

## Benefits

1. **Auditability**: All model changes are logged
2. **Debugging**: Easy to track model lifecycle events
3. **Monitoring**: Real-time signal tracking
4. **Production Ready**: Apache signal handling for deployment
5. **Extensible**: Easy to add custom logic to signals
