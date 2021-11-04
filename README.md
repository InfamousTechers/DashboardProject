# Dashboard

This is a practise project that we used to learn the Java Framework Vaadin.
It is a basic workspace tools application that include tools like a To-do List, Notes, Calculator, Timer and a Calender.

This project was created from https://start.vaadin.com.

## Running and debugging the applcation

### Running the application from the command line.
To run from the command line, use `mvn` and open http://localhost:8080 in your browser.
```
mvn spring-boot:run -f "pom.xml"
```

### Running and debugging the application in Intellij IDEA
- Locate the Application.java class in the Project view. It is in the src folder, under the main package's root.
- Right click on the Application class
- Select "Debug 'Application.main()'" from the list

After the application has started, you can view your it at http://localhost:8080/ in your browser. 
You can now also attach break points in code for debugging purposes, by clicking next to a line number in any source file.

### Running and debugging the application in Eclipse
- Locate the Application.java class in the Package explorer. It is in `src/main/java`, under the main package.
- Right click on the file and select `Debug As` --> `Java Application`.

Do not worry if the debugger breaks at a `SilentExitException`. This is a Spring Boot feature and happens on every startup.

After the application has started, you can view your it at http://localhost:8080/ in your browser.
You can now also attach break points in code for debugging purposes, by clicking next to a line number in any source file.
## Project structure

- `MainView.java` in `src/main/java` contains the navigation setup. It uses [App Layout](https://vaadin.com/components/vaadin-app-layout).
- `views` package in `src/main/java` contains the server-side Java views of your application.
- `views` folder in `frontend/src/` contains the client-side JavaScript views of your application.

## What we've learnt?
This project helped us learn how to use Maven to manage Java projects as we were both new to it. Also got to learn how to utilize pre-built components and merge them with other components to create desired output. This also improved our use of Git and proper collaboration.