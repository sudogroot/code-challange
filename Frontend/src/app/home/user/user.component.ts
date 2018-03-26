import {Component, OnInit, Input} from '@angular/core';
import {UserService} from './user.service';
import {finalize} from 'rxjs/operators';
import {CookieService} from 'ngx-cookie-service';
import {Router} from '@angular/router';


@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss']
})
export class UserComponent implements OnInit {


  userName: string;
  isLoading: boolean;

  cookieExists: boolean = this.cookieService.check('user_name');


  constructor(private userService: UserService, private cookieService: CookieService,
              private router: Router) {
  }

  ngOnInit() {
  }

  submit() {
    this.isLoading = true;
    this.userService.user(this.userName)
      .pipe(finalize(() => {
        this.isLoading = false;
      }))
      .subscribe((r: any) => {
        const result = r;
        this.cookieService.set('user_name', result.user_name);
        if (this.cookieService.check('user_name')) {
          this.router.navigate(['activities']);
        }


      });
  }


}
