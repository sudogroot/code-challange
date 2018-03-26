import {Component, OnInit, EventEmitter, Input, Output} from '@angular/core';
import {Comments} from '@app/models/book-detail';
import {CookieService} from 'ngx-cookie-service';


@Component({
  selector: 'app-comments',
  templateUrl: './comments.component.html',
  styleUrls: ['./comments.component.scss']
})
export class CommentsComponent implements OnInit {


  @Input() comments: Array<Comments>;
  @Input() hidden: string;
  @Output() comment = new EventEmitter<string>();
  newComment: string;
  cookieExists: boolean = this.cookieService.check('user_name');

  constructor(private cookieService: CookieService) {
  }

  ngOnInit() {
  }

  postComment() {
    this.comment.emit(this.newComment);
    this.newComment = '';

  }


}
