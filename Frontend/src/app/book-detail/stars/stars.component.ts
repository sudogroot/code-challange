import {Component, OnInit, EventEmitter, Input, Output} from '@angular/core';
import {CookieService} from 'ngx-cookie-service';


@Component({
  selector: 'app-stars',
  templateUrl: './stars.component.html',
  styleUrls: ['./stars.component.scss']
})
export class StarsComponent implements OnInit {

  @Input() stars: number;
  @Output() stared = new EventEmitter<number>();
  newStars: number;
  cookieExists: boolean = this.cookieService.check('user_name');


  constructor(private cookieService: CookieService) {
  }

  ngOnInit() {
  }


  postStars() {
    this.stared.emit(this.newStars);
    this.newStars = null;

  }


}
