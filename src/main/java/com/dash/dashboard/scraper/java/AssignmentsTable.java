package com.dash.dashboard.scraper.java;

import com.dash.dashboard.views.dashboard.Assignment;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * @author brandonpahla
 * @email brandon.m.paahla@gmail.com
 */
public class AssignmentsTable extends ToolsTables {
    private Connection connection;

    public AssignmentsTable(){
        connection = super.connect();
    }

    @Override
    public ResultSet selectAll() {
        String sql = "SELECT Course, Title, DueDate FROM Assignments";
        ResultSet rs;

        try{
            Statement stmt  = this.connection.createStatement();
            rs    = stmt.executeQuery(sql);
            return rs;
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return null;
    }
    public List<Assignment> AssignmentsList(){
        List<Assignment>  assignments = new ArrayList<>(0);
        try {
            ResultSet rs = this.selectAll();
            // loop through the result set
            while (rs.next()) {
                assignments.add( new Assignment( rs.getString("Course"),
                        rs.getString("Title"),
                        rs.getString("DueDate")));
            }
        }catch (SQLException e){
        }
        return assignments;
    }

    @Override
    public void printAll(){
        ResultSet rs = this.selectAll();

        // loop through the result set
        try {
            while (rs.next()) {
                System.out.println(rs.getString("Course") + "\t" +
                        rs.getString("Title") + "\t" +
                        rs.getString("DueDate"));
            }
        }catch (SQLException e){
            System.out.println(e.getMessage());
        }
    }

}
