#!/usr/bin/perl
# This file was written as an executable to be used in the auto report function
# of csf and lfd. By replacing $YOUR_API_KEY below with your abuseipdb api key,
# allows you to use this code to integrate your csf system with abuseipdb.com
use strict;
use warnings;
use HTTP::Tiny;
use JSON;

# Gather the information from the commandline passed by lfd
my $ports = $ARGV[1];
my $inout = $ARGV[3];
my $message = $ARGV[5];
my $logs = $ARGV[6];
my $trigger = $ARGV[7];
my $comment = $message . "; Ports: " . $ports . "; Direction: " . $inout
    . "; Trigger: " . $trigger . "; Logs: " . $logs;
my $ua = HTTP::Tiny->new;

my $url = 'https://api.abuseipdb.com/api/v2/report';

my $data = {
    ip => $ARGV[0],
    comment => $comment,
    categories => 14
};

my %options = (
   "headers", {
       "Key" => "$YOUR_API_KEY",
       "Accept" => "application/json"
   },
);

my $response = $ua->post_form($url, $data, \%options);
my $json = JSON->new;
my $output = $json->pretty->encode($json->decode($response->{'content'}));

if ($response->{'status'} == 200){
    print "Report Succesful!\n" . $output;
} elsif ($response->{'status'} == 429) {
    print $output;
} elsif ($response->{'status'} == 422) {
    print $output;
} elsif ($response->{'status'} == 401) {
    print $output;
}
