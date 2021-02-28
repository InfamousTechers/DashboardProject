package com.dash.dashboard.views.dashboard;

import com.dash.dashboard.scraper.java.AnnouncementsTable;
import com.dash.dashboard.scraper.java.AssignmentsTable;
import com.dash.dashboard.scraper.java.GradebookTable;
import com.dash.dashboard.scraper.java.TestsTable;
import com.vaadin.flow.component.Component;
//import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.dependency.CssImport;
import com.vaadin.flow.component.grid.Grid;
import com.vaadin.flow.component.grid.GridVariant;
import com.vaadin.flow.component.html.Div;
import com.vaadin.flow.component.html.H3;
import com.vaadin.flow.component.notification.Notification;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.tabs.Tab;
import com.vaadin.flow.component.tabs.Tabs;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

//import com.vaadin.flow.component.orderedlayout.VerticalLayout;
//import com.vaadin.flow.component.textfield.TextField;

import com.vaadin.flow.router.PageTitle;
import com.vaadin.flow.router.Route;
import com.dash.dashboard.views.main.MainView;
import com.vaadin.flow.router.RouteAlias;

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
        Tab emails = new Tab("Announcements");
        Div emailsPage = new Div();
        emailsFunc(emailsPage);
        
        Tab assignments = new Tab("Pending Assignments");
        Div assPage = new Div();
        assFunc(assPage);
        
        Tab tests = new Tab("Upcoming Tests");
        Div testsPage = new Div();
        testsFunc(testsPage);
        
        Tab gradebook = new Tab("Gradebook");
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
        List<Announcement> announcements;
        AnnouncementsTable announcementsTable = new AnnouncementsTable();

        announcements = announcementsTable.announcementsList();
        Grid<Announcement> grid = new Grid<>();

        grid.setItems(announcements);
        grid.addColumn(Announcement::getDate).setHeader("Date");
        grid.addColumn(Announcement::getPreview).setHeader("Announcement");
        grid.addColumn(Announcement::getAuthor).setHeader("Author");
        grid.getColumns().forEach(col -> col.setAutoWidth(true));

        grid.asSingleSelect().addValueChangeListener(evt -> popUpMessage(evt.getValue()));
        grid.addThemeVariants(GridVariant.LUMO_WRAP_CELL_CONTENT, GridVariant.LUMO_NO_BORDER, GridVariant.LUMO_NO_ROW_BORDERS, GridVariant.LUMO_ROW_STRIPES);
        Page.add(new H3("Announcement"));
        Page.add(grid);
    }

    private void popUpMessage(Announcement value) {
        Notification notification = new Notification(
                "Function Coming Soon:" + value.getPreview(), 10000);
        notification.open();
    }

    private void assFunc(Div Page){

        List<Assignment> assignments;
        AssignmentsTable assignmentsTable = new AssignmentsTable();

        assignments = assignmentsTable.AssignmentsList();
        Grid<Assignment> grid = new Grid<>();

        grid.setItems(assignments);
        grid.addColumn(Assignment::getTitle).setHeader("Assignment");
        grid.addColumn(Assignment::getDueDate).setHeader("Due Date");
        grid.addColumn(Assignment::getSite).setHeader("Site");
        grid.getColumns().forEach(col -> col.setAutoWidth(true));

        grid.asSingleSelect().addValueChangeListener(event -> popUpAssMessage(event.getValue()));
        grid.addThemeVariants(GridVariant.LUMO_WRAP_CELL_CONTENT, GridVariant.LUMO_NO_BORDER, GridVariant.LUMO_NO_ROW_BORDERS, GridVariant.LUMO_ROW_STRIPES);
        Page.add(new H3("Assignments"));
        Page.add(grid);
    }

    private void popUpAssMessage(Assignment value) {
        Notification notification = new Notification(value.getDueDate(), 10000);
        notification.open();
    }

    private void testsFunc(Div Page){
        List<Test> tests;
        TestsTable testsTable = new TestsTable();
        tests = testsTable.testList();
        Grid<Test> grid = new Grid<>();
        grid.setItems(tests);
        grid.addColumn(Test::getTitle).setHeader("Test");
        grid.addColumn(Test::getTimeLimit).setHeader("Time Limit");
        grid.addColumn(Test::getDueDate).setHeader("Due Date");
        grid.getColumns().forEach(col -> col.setAutoWidth(true));
        grid.addThemeVariants(GridVariant.LUMO_WRAP_CELL_CONTENT, GridVariant.LUMO_NO_BORDER, GridVariant.LUMO_NO_ROW_BORDERS, GridVariant.LUMO_ROW_STRIPES);
        Page.add(new H3("Tests"));
        Page.add(grid);
    }

    private void gradebookFunc(Div Page){
        List<Gradebook> grades;
        GradebookTable testsTable = new GradebookTable();

        grades = testsTable.gradesList();
        Grid<Gradebook> grid = new Grid<>();

        grid.setItems(grades);
        grid.addColumn(Gradebook::getCourse).setHeader("Course");
        grid.addColumn(Gradebook::getTitle).setHeader("Title");
        grid.addColumn(Gradebook::getMark).setHeader("Mark");
        grid.addColumn(Gradebook::getTotal).setHeader("Total");
        grid.getColumns().forEach(col -> col.setAutoWidth(true));

        grid.asSingleSelect().addValueChangeListener(event -> showPercentage(event.getValue()));
        grid.addThemeVariants(GridVariant.LUMO_WRAP_CELL_CONTENT, GridVariant.LUMO_NO_BORDER, GridVariant.LUMO_NO_ROW_BORDERS, GridVariant.LUMO_ROW_STRIPES);
        Page.add(new H3("Gradebook"));
        Page.add(grid);
    }

    private void showPercentage(Gradebook value) {
        String mark = value.getMark();
        String total = value.getTotal();
        float percentage = 0;
        if (!(mark.equalsIgnoreCase("-"))){
            float markFloat = Float.parseFloat(mark);
            float totalFloat = Float.parseFloat(total);
            percentage = 100*(markFloat/totalFloat);
        }

        if (percentage < 50){
            mark = percentage + " %" + "   Fail";
            Notification notification = new Notification(mark, 10000);
            notification.open();
        }
        else if (percentage > 49 && percentage < 60){
            mark = percentage + " %" + "    Third Class [C]";
            Notification notification = new Notification(mark, 10000);
            notification.open();
        }else if (percentage > 59 && percentage < 70){
            mark = percentage + " %" + "    Second Class (Division 2) [B]";
            Notification notification = new Notification(mark, 10000);
            notification.open();
        }else if (percentage > 69 && percentage < 75){
            mark = percentage + " %" + "    Second Class (Division 1) [B+]";
            Notification notification = new Notification(mark, 10000);
            notification.open();
        }else if (percentage > 74 && percentage < 100.5){
            mark = percentage + " %" + "    First Class [A]";
            Notification notification = new Notification(mark, 10000);
            notification.open();
        }

    }

}
