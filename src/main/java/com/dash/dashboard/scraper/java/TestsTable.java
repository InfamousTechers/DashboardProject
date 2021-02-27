package com.dash.dashboard.scraper.java;

import com.dash.dashboard.views.dashboard.Test;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

/**
 * @author brandonpahla
 * @email brandon.m.paahla@gmail.com
 */
public class TestsTable extends ToolsTables {
    private Connection connection;

    public TestsTable(){
        connection = super.connect();
    }

    public List<Test> testList(){
        List<Test> tests = new ArrayList<>(0);
        try {
            ResultSet rs = this.selectAll();
            if (rs != null) {
                while (rs.next()) {
                    tests.add(new Test(rs.getString("Title"),
                            rs.getString("TimeLimit"),
                            rs.getString("DueDate")));
                }
            }
        }catch (SQLException e){
        }
        return tests;
    }

    @Override
    public ResultSet selectAll() {
        String sql = "SELECT Title, Timelimit, Duedate  FROM Tests";
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

    @Override
    public void printAll() {
        ResultSet rs = this.selectAll();
        // loop through the result set
        try {
            while (rs.next()) {
                System.out.println(rs.getString("Title") + " \t" +
                        rs.getString("TimeLimit") + " \t" +
                        rs.getString("DueDate"));
            }
        }catch (SQLException e){
            System.out.println(e.getMessage());
        }

    }

}
