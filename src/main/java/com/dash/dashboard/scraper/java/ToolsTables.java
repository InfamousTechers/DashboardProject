package com.dash.dashboard.scraper.java;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * @author brandonpahla
 * @email brandon.m.paahla@gmail.com
 */
public abstract class ToolsTables implements Tables {

    @Override
    public Connection connect() {
        Connection conn;
        try {
            conn = DriverManager.getConnection(url);
            return conn;
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }return null;
    }

    public abstract ResultSet selectAll();

    public abstract void printAll();
}
