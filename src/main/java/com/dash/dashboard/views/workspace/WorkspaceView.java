package com.dash.dashboard.views.workspace;

import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.dependency.CssImport;
import com.vaadin.flow.component.html.Div;
// import com.vaadin.flow.component.notification.Notification;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.tabs.Tab;
import com.vaadin.flow.component.tabs.Tabs;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.router.PageTitle;
import com.vaadin.flow.router.Route;
import java.util.HashMap;
import java.util.Map;
import com.dash.dashboard.views.main.MainView;
import com.vaadin.flow.router.RouteAlias;
import com.vaadin.flow.component.Component;

@Route(value = "Workspace", layout = MainView.class)
@PageTitle("Workspace")
@CssImport("./styles/views/dashboard/dashboard-view.css")
@RouteAlias(value = "workspace", layout = MainView.class)
public class WorkspaceView extends HorizontalLayout {

    /**
	 *
	 */
	private static final long serialVersionUID = -7468284506066059747L;
	private Tabs tabs;

    public WorkspaceView() {
        setId("dashboard-view");
        workspaceTabs();
    }

    private void workspaceTabs(){
        // Creating workspace tabs
        Tab todo = new Tab("To-do List");
        Div todoPage = new Div();
        todoFunc(todoPage);
                
        Tab note = new Tab("Notes");
        Div notePage = new Div();
        noteFunc(notePage);
        
        Tab calc = new Tab("Calculator");
        Div calcPage = new Div();
        calcFunc(calcPage);
        
        Tab timer = new Tab("Pomodoro Timer");
        Div timerPage = new Div();
        timerFunc(timerPage);
        
        Tab cal = new Tab("Calender");
        Div calPage = new Div();
        calFunc(calPage);

        Map<Tab, Component> tabsToPages = new HashMap<>();
        tabsToPages.put(todo, todoPage);
        tabsToPages.put(note, notePage);
        tabsToPages.put(calc, calcPage);
        tabsToPages.put(timer, timerPage);
        tabsToPages.put(cal, calPage);
        tabs = new Tabs(todo, note, calc, timer, cal);
        tabs.setFlexGrowForEnclosedTabs(1);
        Div pages = new Div(todoPage, notePage, calcPage, timerPage, calPage);

        tabs.addSelectedChangeListener(event -> {
            tabsToPages.values().forEach(page -> page.setVisible(false));
            Component selectedPage = tabsToPages.get(tabs.getSelectedTab());
            selectedPage.setVisible(true);
        });

        tabs.setSelectedTab(cal);
        tabs.setSelectedTab(todo);

        add(tabs, pages);
    }
    
    /**
     * Functions for the pages
     */

    private void todoFunc(Div Page){
        Page.setText("To-do List");
        // Verticallayout addTask = new Verticallayout();
        // Horizontallayout taskView = new Horizontallayout();
        // Page.add(addTask, taskView);
        
        // TextField task = new TextField();
        // task.setLabel("Task");
        // task.setLabel("What do you have to do?");
        // Button add = new Button("Add", evt -> {

        // });

        
    }

    private void noteFunc(Div Page){
        Page.setText("Notes");
    }

    private void calcFunc(Div Page){
        Page.setText("Calculator");
    }

    private void timerFunc(Div Page){
        Page.setText("Timer");
    }

    private void calFunc(Div Page){
        Page.setText("Calender");
    }

}
