package com.dash.dashboard.views.dashboard;

import com.google.common.collect.Table;
import com.vaadin.flow.component.Component;
//import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.dependency.CssImport;
import com.vaadin.flow.component.grid.Grid;
import com.vaadin.flow.component.html.Div;
//import com.vaadin.flow.component.notification.Notification;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.tabs.Tab;
import com.vaadin.flow.component.tabs.Tabs;
import java.util.HashMap;
import java.util.Map;
//import com.vaadin.flow.component.orderedlayout.VerticalLayout;
//import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.router.PageTitle;
import com.vaadin.flow.router.Route;
import com.dash.dashboard.views.main.MainView;
import com.vaadin.flow.router.RouteAlias;
import net.bytebuddy.implementation.bind.annotation.AllArguments;
import org.springframework.web.servlet.View;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Route(value = "Dashboard", layout = MainView.class)
@PageTitle("Dashboard")
@CssImport("./styles/views/dashboard/dashboard-view.css")
@RouteAlias(value = "", layout = MainView.class)
public class DashboardView extends HorizontalLayout {

    /**
	 *
	 */

	private static final long serialVersionUID = -7468284506066059747L;
    private Tabs tabs;

    public DashboardView() {
        setId("dashboard-view");
        dashTabs();
    }

    private void dashTabs(){
        Tab emails = new Tab("AnnouncementsTable");
        Div emailsPage = new Div();
        emailsFunc(emailsPage);
        
        Tab assignments = new Tab("Pending AssignmentsTable");
        Div assPage = new Div();
        assFunc(assPage);
        
        Tab tests = new Tab("Upcoming TestsTable");
        Div testsPage = new Div();
        testsFunc(testsPage);
        
        Tab gradebook = new Tab("GradebookTable");
        Div gradebookPage = new Div();
        gradebookFunc(gradebookPage);
        
        Map<Tab, Component> tabsToPages = new HashMap<>();
        tabsToPages.put(emails, emailsPage);
        tabsToPages.put(assignments, assPage);
        tabsToPages.put(tests, testsPage);
        tabsToPages.put(gradebook, gradebookPage);
        tabs = new Tabs(emails, assignments, tests, gradebook);
        tabs.setFlexGrowForEnclosedTabs(1);
        Div pages = new Div(emailsPage, assPage, testsPage, gradebookPage);

        tabs.addSelectedChangeListener(event -> {
            tabsToPages.values().forEach(page -> page.setVisible(false));
            Component selectedPage = tabsToPages.get(tabs.getSelectedTab());
            selectedPage.setVisible(true);
        });

        tabs.setSelectedTab(tests);
        tabs.setSelectedTab(emails);

        add(tabs, pages);
    }

    private void emailsFunc(Div Page){
        Page.setText("Emails");
    }
    
    private void assFunc(Div Page){
        Page.setText("AssignmentsTable");
    }

    private void testsFunc(Div Page){
        Page.setText("TestsTable");
    }

    private void gradebookFunc(Div Page){
        Page.setText("GradebookTable");
    }

}
