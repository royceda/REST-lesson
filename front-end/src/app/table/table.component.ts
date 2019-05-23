import { Component, OnInit } from '@angular/core';
import { flight } from '../map/map.component'



@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {

  
  flights: flight[] = [
    {
      op_nb : "AF1000",
      origin : "CDG",
      destination : "MAD",
      ori_lat : 43,
      ori_lng : 21,
      dst_lat : 23,
      dst_lng : 40
    },
    {
      op_nb : "AF1001",
      origin : "CDG",
      destination : "AJA",
      ori_lat : 51.673858,
      ori_lng : 7.815982,
      dst_lat : 51.723858,
      dst_lng : 7.895982
    }
  ]

  constructor() { }

  ngOnInit() {
  }

}
