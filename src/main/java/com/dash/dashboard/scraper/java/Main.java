package com.dash.dashboard.scraper.java;

/**
 * @author brandonpahla
 * @email brandon.m.paahla@gmail.com
 */

public class Main {
    public static void main(String[] args) {
        GradebookTable gradebookTable = new GradebookTable();
        gradebookTable.printAll();

        AnnouncementsTable announcementsTable = new AnnouncementsTable();
        announcementsTable.printAll();

        AssignmentsTable assignmentsTable = new AssignmentsTable();
        assignmentsTable.printAll();

        TestsTable testsTable = new TestsTable();
        testsTable.printAll();
    }

}
